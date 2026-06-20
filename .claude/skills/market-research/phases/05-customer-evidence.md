# Phase 5: Customer Evidence Discovery — Subagent Research Prompt (Optional)

> **When to load:** Phase 5 of market research, if the operator chooses to run it. Sent to a Sonnet subagent.
> **Purpose:** Find where social proof, case studies, and customer evidence exist online. URL discovery, not analysis.
> **When to run:** When the engagement needs social proof for messaging, when the client has thin third-party validation, or when building enrichment pipelines.

---

You are conducting customer evidence discovery for a B2B company. Your job is to find all relevant URLs containing customer testimonials, case studies, reviews, and social proof. This is a discovery task — find and catalog the evidence, don't analyze it.

You have access to web search — use it extensively with advanced search operators.

## Context

You will receive the company name and may receive market context identifying industry-specific review platforms relevant to this company's market. Check those platforms in addition to the standard ones below.

## Search Patterns

### Company Website
Search for these URL patterns on the company website:
- /case-studies, /customers, /success-stories, /resources/case-studies
- /customer-stories, /testimonials, /results, /customer-success
- /blog + "case study" or "success story"

Use advanced search operators:
- `site:example.com "case study"`
- `site:example.com "success story"` or `"customer story"`
- `site:example.com intitle:"case study"`
- `site:example.com inurl:case-study`
- `site:example.com filetype:pdf "case study"`

### Review Platforms
Search for the company profile on:

**Software Reviews:**
- G2 (g2.com/products/)
- Capterra (capterra.com/p/)
- TrustRadius (trustradius.com/products/)
- GetApp (getapp.com)
- PeerSpot (peerspot.com/products/)
- Gartner Peer Insights (gartner.com/reviews/)

**B2B Review Sites:**
- SourceForge, Crozdesk, SelectHub, FeaturedCustomers

**Industry-Specific Platforms:**
- Check market context for industry-specific review sites, directories, or communities relevant to this company's vertical.

### Social Proof
**LinkedIn:**
- Company page posts mentioning customers or results
- Employee posts about customer wins
- Customer employees posting about using the product

**YouTube:**
- Company channel (testimonial videos, case study videos, webinars with customers)
- Search: "[company name]" + "case study" or "testimonial" or "review"

**Other:**
- SlideShare presentations featuring customer results
- Podcast appearances discussing customer outcomes

### News and PR
- `site:prnewswire.com "[company name]" "customer"`
- `site:businesswire.com "[company name]"`
- `"[company name]" AND ("implements" OR "deploys" OR "selects" OR "chooses")`
- `"[company name]" AND "ROI" AND ("achieved" OR "realized")`
- Crunchbase news section

## Output Format

```markdown
# Customer Evidence: [Company Name]

## Official Case Studies
| URL | Content Type | Customer Named | Industry | Last Updated |
|-----|-------------|---------------|----------|-------------|
| ... | ... | ... | ... | ... |

## Review Platform Profiles
| Platform | URL | Review Count | Avg Rating | Access |
|----------|-----|-------------|-----------|--------|
| ... | ... | ... | ... | Public/Registration |

## Social Proof
| Platform | URL | Content Type | Notable |
|----------|-----|-------------|---------|
| ... | ... | ... | ... |

## News and PR Coverage
| URL | Headline | Date | Customer Named |
|-----|---------|------|---------------|
| ... | ... | ... | ... |

## Summary
- Total case studies found: [N]
- Total review platforms with presence: [N]
- Review count across platforms: [N]
- Notable gaps: [What's missing — no video testimonials? No industry-specific reviews?]
```

Verify each URL is active. Note any access restrictions (registration required, paywalled).
