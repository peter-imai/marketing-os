#!/usr/bin/env python3
"""
Markdown → Google Doc converter.

Converts a markdown file (or stdin) into a formatted Google Doc via `gws` CLI.
Creates a new doc, writes content with proper formatting (headings, bold, italic,
lists, tables, blockquotes) and applies a professional document style.

Usage:
    python3 md_to_gdoc.py <file> [--title "Doc Title"] [--style clean|none]
    python3 md_to_gdoc.py <file> --doc-id <existing_doc_id>
    python3 md_to_gdoc.py <file> --doc-id <id> --tab-id <tab_id>  # write to specific tab
    python3 md_to_gdoc.py <file> --font "Source Sans 3"
    cat content.md | python3 md_to_gdoc.py - --title "Doc Title"

Styles:
    clean — Inter font, heading hierarchy, table styling, blockquotes (default)
    none  — Google Docs defaults (structural formatting only)

Returns JSON with documentId and URL on success.
"""

import json
import re
import subprocess
import sys
import argparse


# ---------------------------------------------------------------------------
# Style definitions
# ---------------------------------------------------------------------------

def _rgb(r, g, b):
    """Build OptionalColor dict for the Google Docs API."""
    return {'color': {'rgbColor': {'red': r, 'green': g, 'blue': b}}}


# "Clean" style — professional, understated, readable.
# Font: Inter (Google Fonts). Falls back to default if unavailable.
# Color palette: navy/slate heading hierarchy, dark gray body.
CLEAN_STYLE = {
    'font': 'Inter',
    'body': {
        'fontSize': 11,
        'color': (0.20, 0.20, 0.20),           # #333333
        'lineSpacing': 115,                      # 1.15x
        'spaceBelow': 4,                         # pt after each paragraph
    },
    'headings': {
        1: {'fontSize': 20, 'color': (0.106, 0.149, 0.192), 'spaceAbove': 6, 'spaceBelow': 4},
        2: {'fontSize': 15, 'color': (0.141, 0.192, 0.247), 'spaceAbove': 16, 'spaceBelow': 4},
        3: {'fontSize': 12, 'color': (0.204, 0.286, 0.369), 'spaceAbove': 12, 'spaceBelow': 3},
        4: {'fontSize': 11, 'color': (0.204, 0.286, 0.369), 'spaceAbove': 10, 'spaceBelow': 2},
        5: {'fontSize': 11, 'color': (0.298, 0.376, 0.455), 'spaceAbove': 8, 'spaceBelow': 2,
            'italic': True},
        6: {'fontSize': 10, 'color': (0.400, 0.475, 0.545), 'spaceAbove': 6, 'spaceBelow': 2},
    },
    'table': {
        'header_bg': (0.918, 0.929, 0.937),     # #EAECEF  light gray
        'border_color': (0.835, 0.855, 0.875),  # #D5DADF  subtle border
        'border_width': 0.5,                     # pt
        'padding_v': 5,                          # pt  top/bottom cell padding
        'padding_h': 7,                          # pt  left/right cell padding
    },
    'blockquote': {
        'border_color': (0.741, 0.765, 0.780),  # #BDC3C7  left accent bar
        'border_width': 3,                       # pt
        'border_padding': 10,                    # pt  space between bar and text
        'color': (0.333, 0.333, 0.333),          # #555555  muted text
    },
}

STYLES = {'clean': CLEAN_STYLE}


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------

def is_separator_row(line: str) -> bool:
    """Check if a table line is a separator row (|---|---|)."""
    stripped = line.strip().strip('|')
    return all(re.match(r'\s*:?-+:?\s*$', c) for c in stripped.split('|'))


def parse_table_row(line: str) -> list[str]:
    """Parse a markdown table row into cell values."""
    return [c.strip() for c in line.strip().strip('|').split('|')]


def parse_markdown(text: str) -> list[dict]:
    """Parse markdown into structured blocks."""
    # Strip YAML frontmatter
    text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)

    blocks = []
    lines = text.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Horizontal rule — skip
        if re.match(r'^[-*_]{3,}\s*$', line.strip()) and not line.strip().startswith('|'):
            i += 1
            continue

        # Table
        if re.match(r'^\|.+\|', line.strip()):
            table_lines = []
            while i < len(lines) and re.match(r'^\|.+\|', lines[i].strip()):
                table_lines.append(lines[i])
                i += 1
            if len(table_lines) >= 2:
                headers = parse_table_row(table_lines[0])
                start = 2 if is_separator_row(table_lines[1]) else 1
                rows = [parse_table_row(tl) for tl in table_lines[start:]]
                blocks.append({'type': 'table', 'headers': headers, 'rows': rows})
            continue

        # Blockquote (consecutive > lines)
        if re.match(r'^>\s?', line):
            bq_lines = []
            while i < len(lines) and re.match(r'^>', lines[i]):
                content = re.sub(r'^>\s?', '', lines[i]).strip()
                if content:
                    bq_lines.append(content)
                i += 1
            if bq_lines:
                blocks.append({'type': 'blockquote', 'text': ' '.join(bq_lines)})
            continue

        # Heading
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            blocks.append({'type': f'heading_{len(m.group(1))}', 'text': m.group(2).strip()})
            i += 1
            continue

        # Unordered list
        m = re.match(r'^(\s*)[-*+]\s+(.+)$', line)
        if m:
            blocks.append({
                'type': 'bullet', 'text': m.group(2).strip(),
                'nesting': len(m.group(1)) // 2
            })
            i += 1
            continue

        # Ordered list
        m = re.match(r'^(\s*)\d+\.\s+(.+)$', line)
        if m:
            blocks.append({
                'type': 'ordered', 'text': m.group(2).strip(),
                'nesting': len(m.group(1)) // 2
            })
            i += 1
            continue

        # Empty line
        if line.strip() == '':
            i += 1
            continue

        # Paragraph (collect continuation lines)
        para = [line]
        i += 1
        while (i < len(lines) and lines[i].strip() != ''
               and not re.match(r'^#{1,6}\s', lines[i])
               and not re.match(r'^[-*+]\s', lines[i])
               and not re.match(r'^\d+\.\s', lines[i])
               and not re.match(r'^\|.+\|', lines[i].strip())
               and not re.match(r'^>', lines[i])):
            para.append(lines[i])
            i += 1
        blocks.append({'type': 'paragraph', 'text': ' '.join(l.strip() for l in para)})

    return blocks


# ---------------------------------------------------------------------------
# Inline formatting
# ---------------------------------------------------------------------------

def find_inline_formats(text: str) -> tuple[str, list[dict]]:
    """Extract bold/italic markers, return (plain_text, format_ranges)."""
    formats = []
    plain = ''
    i = 0
    while i < len(text):
        # Bold+italic (***text***)
        m = re.match(r'\*{3}(.+?)\*{3}|_{3}(.+?)_{3}', text[i:])
        if m:
            content = m.group(1) or m.group(2)
            start = len(plain); plain += content
            formats.append({'start': start, 'end': len(plain), 'bold': True, 'italic': True})
            i += m.end(); continue

        # Bold (**text**)
        m = re.match(r'\*{2}(.+?)\*{2}|_{2}(.+?)_{2}', text[i:])
        if m:
            content = m.group(1) or m.group(2)
            start = len(plain); plain += content
            formats.append({'start': start, 'end': len(plain), 'bold': True})
            i += m.end(); continue

        # Italic (*text*)
        m = re.match(r'\*(.+?)\*|_(.+?)_', text[i:])
        if m:
            content = m.group(1) or m.group(2)
            start = len(plain); plain += content
            formats.append({'start': start, 'end': len(plain), 'italic': True})
            i += m.end(); continue

        plain += text[i]
        i += 1
    return plain, formats


# ---------------------------------------------------------------------------
# Google Docs API request building
# ---------------------------------------------------------------------------

HEADING_STYLE_MAP = {
    f'heading_{i}': f'HEADING_{i}' for i in range(1, 7)
}


def _base_text_style(doc_style: dict) -> dict:
    """Return the base text style dict + fields string from a doc_style config."""
    body = doc_style['body']
    cr, cg, cb = body['color']
    return {
        'style': {
            'weightedFontFamily': {'fontFamily': doc_style['font'], 'weight': 400},
            'fontSize': {'magnitude': body['fontSize'], 'unit': 'PT'},
            'foregroundColor': _rgb(cr, cg, cb),
        },
        'fields': 'weightedFontFamily,fontSize,foregroundColor',
    }


def build_text_requests(blocks: list[dict], insert_at: int = 1,
                        doc_style=None, after_table: bool = False) -> tuple[list[dict], int]:
    """Build requests for a run of text blocks. Returns (requests, text_length)."""
    full_text = ''
    segments = []

    for block in blocks:
        plain, ifmts = find_inline_formats(block['text'])
        tw = plain + '\n'
        start = len(full_text)
        segments.append({
            'start': start, 'end': start + len(tw),
            'type': block['type'], 'nesting': block.get('nesting', 0),
            'inline_formats': ifmts,
        })
        full_text += tw

    if not full_text:
        return [], 0

    requests = [{'insertText': {'location': {'index': insert_at}, 'text': full_text}}]
    offset = insert_at

    # --- Base document style applied to entire text segment ---
    if doc_style:
        body = doc_style['body']
        text_end = insert_at + len(full_text)
        cr, cg, cb = body['color']

        # Base paragraph style (line spacing, space after)
        requests.append({
            'updateParagraphStyle': {
                'range': {'startIndex': insert_at, 'endIndex': text_end},
                'paragraphStyle': {
                    'lineSpacing': body['lineSpacing'],
                    'spaceBelow': {'magnitude': body['spaceBelow'], 'unit': 'PT'},
                },
                'fields': 'lineSpacing,spaceBelow'
            }
        })

        # Base text style (font, size, color)
        base = _base_text_style(doc_style)
        requests.append({
            'updateTextStyle': {
                'range': {'startIndex': insert_at, 'endIndex': text_end - 1},
                'textStyle': base['style'],
                'fields': base['fields'],
            }
        })

    # Extra breathing room on first paragraph after a table
    if after_table and segments:
        first = segments[0]
        fs = first['start'] + offset
        fe = first['end'] + offset
        requests.append({
            'updateParagraphStyle': {
                'range': {'startIndex': fs, 'endIndex': fe},
                'paragraphStyle': {
                    'spaceAbove': {'magnitude': 10, 'unit': 'PT'},
                },
                'fields': 'spaceAbove'
            }
        })

    bq_cfg = doc_style.get('blockquote') if doc_style else None

    for seg in segments:
        s = seg['start'] + offset
        e = seg['end'] + offset

        # --- Headings ---
        if seg['type'] in HEADING_STYLE_MAP:
            # Set heading identity (appears in doc outline, etc.)
            requests.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': s, 'endIndex': e},
                    'paragraphStyle': {'namedStyleType': HEADING_STYLE_MAP[seg['type']]},
                    'fields': 'namedStyleType'
                }
            })
            # Visual style overrides
            if doc_style:
                level = int(seg['type'].split('_')[1])
                h = doc_style['headings'].get(level)
                if h:
                    hr, hg, hb = h['color']
                    requests.append({
                        'updateParagraphStyle': {
                            'range': {'startIndex': s, 'endIndex': e},
                            'paragraphStyle': {
                                'spaceAbove': {'magnitude': h['spaceAbove'], 'unit': 'PT'},
                                'spaceBelow': {'magnitude': h['spaceBelow'], 'unit': 'PT'},
                                'keepWithNext': True,
                            },
                            'fields': 'spaceAbove,spaceBelow,keepWithNext'
                        }
                    })
                    ts = {
                        'fontSize': {'magnitude': h['fontSize'], 'unit': 'PT'},
                        'bold': True,
                        'foregroundColor': _rgb(hr, hg, hb),
                    }
                    flds = 'fontSize,bold,foregroundColor'
                    if h.get('italic'):
                        ts['italic'] = True
                        flds += ',italic'
                    requests.append({
                        'updateTextStyle': {
                            'range': {'startIndex': s, 'endIndex': e - 1},
                            'textStyle': ts,
                            'fields': flds
                        }
                    })

        # --- Bullets ---
        elif seg['type'] == 'bullet':
            requests.append({
                'createParagraphBullets': {
                    'range': {'startIndex': s, 'endIndex': e},
                    'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'
                }
            })
            if seg['nesting'] > 0:
                requests.append({
                    'updateParagraphStyle': {
                        'range': {'startIndex': s, 'endIndex': e},
                        'paragraphStyle': {
                            'indentStart': {'magnitude': 36 * (seg['nesting'] + 1), 'unit': 'PT'}
                        },
                        'fields': 'indentStart'
                    }
                })

        # --- Ordered lists ---
        elif seg['type'] == 'ordered':
            requests.append({
                'createParagraphBullets': {
                    'range': {'startIndex': s, 'endIndex': e},
                    'bulletPreset': 'NUMBERED_DECIMAL_ALPHA_ROMAN'
                }
            })

        # --- Blockquotes ---
        elif seg['type'] == 'blockquote':
            para = {}
            flds = []
            if bq_cfg:
                br, bg, bb = bq_cfg['border_color']
                para['borderLeft'] = {
                    'color': _rgb(br, bg, bb),
                    'width': {'magnitude': bq_cfg['border_width'], 'unit': 'PT'},
                    'padding': {'magnitude': bq_cfg['border_padding'], 'unit': 'PT'},
                    'dashStyle': 'SOLID',
                }
                flds.append('borderLeft')
            else:
                para['indentStart'] = {'magnitude': 24, 'unit': 'PT'}
                flds.append('indentStart')

            requests.append({
                'updateParagraphStyle': {
                    'range': {'startIndex': s, 'endIndex': e},
                    'paragraphStyle': para,
                    'fields': ','.join(flds)
                }
            })
            # Muted text color for styled blockquotes
            if bq_cfg:
                qr, qg, qb = bq_cfg['color']
                requests.append({
                    'updateTextStyle': {
                        'range': {'startIndex': s, 'endIndex': e - 1},
                        'textStyle': {'foregroundColor': _rgb(qr, qg, qb)},
                        'fields': 'foregroundColor'
                    }
                })

        # --- Inline bold/italic ---
        for fmt in seg['inline_formats']:
            fs = seg['start'] + fmt['start'] + offset
            fe = seg['start'] + fmt['end'] + offset
            ts, fl = {}, []
            if fmt.get('bold'):
                ts['bold'] = True; fl.append('bold')
            if fmt.get('italic'):
                ts['italic'] = True; fl.append('italic')
            if ts:
                requests.append({
                    'updateTextStyle': {
                        'range': {'startIndex': fs, 'endIndex': fe},
                        'textStyle': ts, 'fields': ','.join(fl)
                    }
                })

    return requests, len(full_text)


def build_table_requests(table_block: dict, insert_at: int = 1,
                         doc_style=None) -> tuple[list[dict], int]:
    """Build requests for a table block including cell styling.

    Table cell index formula for an R-row, C-column table inserted at index I:
      cell_content_index = I + 4 + r * (1 + 2*C) + 2*c

    Returns (requests, total_index_size).
    """
    headers = table_block['headers']
    rows = table_block['rows']
    num_cols = len(headers)
    total_rows = 1 + len(rows)

    all_rows = [headers] + rows
    for row in all_rows:
        while len(row) < num_cols:
            row.append('')

    requests = [{'insertTable': {
        'rows': total_rows, 'columns': num_cols,
        'location': {'index': insert_at}
    }}]

    # Build base text style for table cells
    base_ts = None
    if doc_style:
        base_ts = _base_text_style(doc_style)

    # Insert cell text (forward order with cumulative offset)
    text_offset = 0
    format_reqs = []

    for r in range(total_rows):
        for c in range(num_cols):
            base_idx = insert_at + 4 + r * (1 + 2 * num_cols) + 2 * c
            idx = base_idx + text_offset
            raw = all_rows[r][c]
            if not raw:
                continue

            plain, ifmts = find_inline_formats(raw)
            if not plain:
                continue

            requests.append({
                'insertText': {'location': {'index': idx}, 'text': plain}
            })

            # Text styling: bold for headers + font for all cells
            if r == 0:
                # Header: bold + base font
                ts = {'bold': True}
                flds = ['bold']
                if base_ts:
                    ts.update(base_ts['style'])
                    flds.extend(base_ts['fields'].split(','))
                format_reqs.append({
                    'updateTextStyle': {
                        'range': {'startIndex': idx, 'endIndex': idx + len(plain)},
                        'textStyle': ts, 'fields': ','.join(flds)
                    }
                })
            elif base_ts:
                # Data cells: base font only
                format_reqs.append({
                    'updateTextStyle': {
                        'range': {'startIndex': idx, 'endIndex': idx + len(plain)},
                        'textStyle': base_ts['style'],
                        'fields': base_ts['fields'],
                    }
                })
            else:
                # No style — bold header only (original behavior)
                if r == 0:
                    format_reqs.append({
                        'updateTextStyle': {
                            'range': {'startIndex': idx, 'endIndex': idx + len(plain)},
                            'textStyle': {'bold': True}, 'fields': 'bold'
                        }
                    })

            # Inline formatting overrides
            for fmt in ifmts:
                fs, fe = idx + fmt['start'], idx + fmt['end']
                ts, fl = {}, []
                if fmt.get('bold'):
                    ts['bold'] = True; fl.append('bold')
                if fmt.get('italic'):
                    ts['italic'] = True; fl.append('italic')
                if ts:
                    format_reqs.append({
                        'updateTextStyle': {
                            'range': {'startIndex': fs, 'endIndex': fe},
                            'textStyle': ts, 'fields': ','.join(fl)
                        }
                    })

            text_offset += len(plain)

    requests.extend(format_reqs)

    # --- Table cell styling ---
    tbl = doc_style.get('table') if doc_style else None
    if tbl:
        # Table element starts 1 index after the insert location
        table_start = insert_at + 1

        # Header row background
        hr, hg, hb = tbl['header_bg']
        requests.append({
            'updateTableCellStyle': {
                'tableRange': {
                    'tableCellLocation': {
                        'tableStartLocation': {'index': table_start},
                        'rowIndex': 0, 'columnIndex': 0,
                    },
                    'rowSpan': 1, 'columnSpan': num_cols,
                },
                'tableCellStyle': {'backgroundColor': _rgb(hr, hg, hb)},
                'fields': 'backgroundColor'
            }
        })

        # All cells: padding + thin borders
        br, bg, bb = tbl['border_color']
        border = {
            'color': _rgb(br, bg, bb),
            'width': {'magnitude': tbl['border_width'], 'unit': 'PT'},
            'dashStyle': 'SOLID',
        }
        requests.append({
            'updateTableCellStyle': {
                'tableRange': {
                    'tableCellLocation': {
                        'tableStartLocation': {'index': table_start},
                        'rowIndex': 0, 'columnIndex': 0,
                    },
                    'rowSpan': total_rows, 'columnSpan': num_cols,
                },
                'tableCellStyle': {
                    'paddingTop': {'magnitude': tbl['padding_v'], 'unit': 'PT'},
                    'paddingBottom': {'magnitude': tbl['padding_v'], 'unit': 'PT'},
                    'paddingLeft': {'magnitude': tbl['padding_h'], 'unit': 'PT'},
                    'paddingRight': {'magnitude': tbl['padding_h'], 'unit': 'PT'},
                    'borderTop': border, 'borderBottom': border,
                    'borderLeft': border, 'borderRight': border,
                },
                'fields': ('paddingTop,paddingBottom,paddingLeft,paddingRight,'
                           'borderTop,borderBottom,borderLeft,borderRight')
            }
        })

    table_size = 3 + total_rows * (1 + 2 * num_cols) + text_offset
    return requests, table_size


def blocks_to_requests(blocks: list[dict], style_name: str = 'clean',
                       font_override: str = None) -> list[dict]:
    """Convert parsed blocks into Google Docs API batchUpdate requests."""
    doc_style = STYLES.get(style_name) if style_name != 'none' else None

    # Apply font override
    if doc_style and font_override:
        doc_style = {**doc_style, 'font': font_override}

    # Group into segments (text runs vs tables)
    segments = []
    current_text = []
    for block in blocks:
        if block['type'] == 'table':
            if current_text:
                segments.append(('text', current_text))
                current_text = []
            segments.append(('table', block))
        else:
            current_text.append(block)
    if current_text:
        segments.append(('text', current_text))

    # Content requests — reverse insertion at index 1
    all_requests = []
    for i, (seg_type, seg_data) in enumerate(reversed(segments)):
        orig_idx = len(segments) - 1 - i
        follows_table = orig_idx > 0 and segments[orig_idx - 1][0] == 'table'

        if seg_type == 'text':
            reqs, _ = build_text_requests(seg_data, insert_at=1, doc_style=doc_style,
                                          after_table=follows_table)
        else:
            reqs, _ = build_table_requests(seg_data, insert_at=1, doc_style=doc_style)
        all_requests.extend(reqs)

    return all_requests


# ---------------------------------------------------------------------------
# Google Docs API via gws CLI
# ---------------------------------------------------------------------------

def _filter_keyring_lines(stdout: str) -> str:
    """Strip the 'Using keyring backend' diagnostic line from gws output."""
    return '\n'.join(l for l in stdout.strip().split('\n') if not l.startswith('Using keyring'))


def create_doc(title: str) -> str:
    """Create a new Google Doc and return its document ID."""
    result = subprocess.run(
        ['gws', 'docs', 'documents', 'create', '--json', json.dumps({'title': title})],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error creating doc: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(_filter_keyring_lines(result.stdout))['documentId']


def get_tab_end_index(doc_id: str, tab_id: str) -> int:
    """Get the last content index in a specific tab."""
    result = subprocess.run(
        ['gws', 'docs', 'documents', 'get',
         '--params', json.dumps({'documentId': doc_id, 'includeTabsContent': True})],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error reading doc: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    doc = json.loads(_filter_keyring_lines(result.stdout))
    for tab in doc.get('tabs', []):
        if tab.get('tabProperties', {}).get('tabId') == tab_id:
            content = tab.get('documentTab', {}).get('body', {}).get('content', [])
            if content:
                return content[-1].get('endIndex', 1)
        # Check child tabs
        for child in tab.get('childTabs', []):
            if child.get('tabProperties', {}).get('tabId') == tab_id:
                content = child.get('documentTab', {}).get('body', {}).get('content', [])
                if content:
                    return content[-1].get('endIndex', 1)
    print(f"Error: tab '{tab_id}' not found in document", file=sys.stderr)
    sys.exit(1)


def inject_tab_id(requests: list[dict], tab_id: str) -> list[dict]:
    """Add tabId to all location and range objects in batchUpdate requests."""
    if not tab_id:
        return requests
    for req in requests:
        for key, value in req.items():
            if not isinstance(value, dict):
                continue
            # Direct location (insertText, insertTable)
            if 'location' in value and isinstance(value['location'], dict):
                value['location']['tabId'] = tab_id
            # Direct range (updateTextStyle, updateParagraphStyle, deleteContentRange)
            if 'range' in value and isinstance(value['range'], dict):
                value['range']['tabId'] = tab_id
            # Table cell operations
            if 'tableRange' in value:
                tr = value['tableRange']
                if 'tableCellLocation' in tr:
                    tcl = tr['tableCellLocation']
                    if 'tableStartLocation' in tcl:
                        tcl['tableStartLocation']['tabId'] = tab_id
    return requests


def write_to_doc(doc_id: str, requests: list[dict]) -> dict:
    """Apply batchUpdate requests to a document."""
    result = subprocess.run(
        ['gws', 'docs', 'documents', 'batchUpdate',
         '--params', json.dumps({'documentId': doc_id}),
         '--json', json.dumps({'requests': requests})],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        # Filter keyring noise from error output
        stderr = result.stderr.replace('Using keyring backend: keyring\n', '').strip()
        stdout = result.stdout.strip()
        error_detail = stderr or stdout
        print(f"Error writing to doc: {error_detail}", file=sys.stderr)
        sys.exit(1)
    return json.loads(_filter_keyring_lines(result.stdout))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Convert markdown to a formatted Google Doc')
    parser.add_argument('file', help='Markdown file path, or - for stdin')
    parser.add_argument('--title', help='Document title (default: first heading or filename)')
    parser.add_argument('--doc-id', help='Write to an existing doc instead of creating one')
    parser.add_argument('--tab-id', help='Target a specific tab (requires --doc-id)')
    parser.add_argument('--style', choices=['clean', 'none'], default='clean',
                        help='Document style preset (default: clean)')
    parser.add_argument('--font', help='Override font family (default: Inter)')
    args = parser.parse_args()

    # Read input
    if args.file == '-':
        md_text = sys.stdin.read()
    else:
        with open(args.file) as f:
            md_text = f.read()

    # Parse
    blocks = parse_markdown(md_text)
    if not blocks:
        print('{"error": "No content found in input"}', file=sys.stderr)
        sys.exit(1)

    # Title
    title = args.title
    if not title:
        for b in blocks:
            if b.get('type', '').startswith('heading'):
                title = b.get('text', '')
                break
        if not title:
            title = args.file if args.file != '-' else 'Untitled Document'

    # Validate tab-id requires doc-id
    if args.tab_id and not args.doc_id:
        print('Error: --tab-id requires --doc-id', file=sys.stderr)
        sys.exit(1)

    # Build requests
    requests = blocks_to_requests(blocks, style_name=args.style, font_override=args.font)

    # Inject tab targeting if specified
    if args.tab_id:
        requests = inject_tab_id(requests, args.tab_id)

    # Create or use existing doc
    doc_id = args.doc_id or create_doc(title)

    # If targeting a tab, clear existing content first
    if args.tab_id:
        end_idx = get_tab_end_index(doc_id, args.tab_id)
        if end_idx > 2:  # More than just the trailing newline
            clear_req = {'deleteContentRange': {
                'range': {'startIndex': 1, 'endIndex': end_idx - 1, 'tabId': args.tab_id}
            }}
            write_to_doc(doc_id, [clear_req])

    # Write
    write_to_doc(doc_id, requests)

    # Output
    url = f"https://docs.google.com/document/d/{doc_id}/edit"
    print(json.dumps({
        'documentId': doc_id, 'url': url, 'title': title,
        'blocks': len(blocks), 'requests': len(requests),
        'style': args.style,
    }, indent=2))


if __name__ == '__main__':
    main()
