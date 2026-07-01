---
step: 5
title: "Deliver — format-specific delivery mechanism"
next: null
reads:
  - contacts.yaml (email — already in context)
writes:
  - Gmail draft or sent message (email format)
  - File in workspaces/[workspace]/artifacts/ (doc/persuasive format)
---

# Step 5: Deliver

**Goal:** Get the approved composition to its destination. Each format has its own delivery mechanism.

---

## Rules

- **No delivery without operator approval.** Step 4's review gate must be passed.
- **Default to the safest delivery.** Email → Gmail draft (not send). Doc/persuasive → file.
- **Confirm delivery.** Always tell the operator what happened and where to find it.

---

## Instructions

### Email Format

**Default path: Gmail draft.**

1. Confirm delivery method: "Create as Gmail draft? (default) Or send directly?"

2. **Gmail draft** (default):
   ```
   Use: draft_gmail_message
   Parameters: user_google_email, to, cc, subject, body, from_email (if alias),
               thread_id + in_reply_to + references (if replying)
   ```
   The operator opens Gmail, reviews one more time, hits send.

3. **Direct send** (only when explicitly requested):
   ```
   Use: send_gmail_message
   (Same parameters — triggers permission confirmation gate)
   ```

4. **Fallback: File-based delivery** (Gmail MCP unavailable):
   - Save the full email (metadata header + body) to `workspaces/[workspace]/artifacts/YYYY-MM-DD-[topic]-email.md`
   - Tell the operator: "Gmail MCP isn't available. Email saved as a file — copy the body into your email client to send."

5. **After delivery:** Confirm with message/draft ID (Gmail path) or file path (fallback). If the operator wants a local copy after Gmail delivery, save to artifacts.

### Data Writeup Format

1. **Save to file.** Default: `workspaces/[workspace]/artifacts/YYYY-MM-DD-[topic].md`
   - If the operator specified a different path (e.g., updating an existing doc), use that.

2. **Offer Google Docs publish:** "Want me to push this to Google Docs?"
   - If yes: execute `.claude/helpers.md#Publish-To-Google-Docs`
   - Return the Google Docs URL.

3. **Confirm:** "Saved to [path]. [Google Docs URL if published.]"

### Persuasive Format

1. **Save to file.** Default: `workspaces/[workspace]/artifacts/YYYY-MM-DD-[topic].md`
   - For landing page copy specifically: `workspaces/[workspace]/landing-page/copy.md`
   - **Separate copy from layout.** The copy document is the argument in prose form. How it maps to a web page or email template is a separate decision.

2. **Offer Google Docs publish:** Same as data writeup.

3. **Confirm:** "Saved to [path]. [Google Docs URL if published.]"

---

## Post-Delivery

After delivery, briefly note:
- What was delivered and where
- Voice scores from Step 4 (one line: "Voice: 32/40")
- Any corrections that were applied to kernel/playbook
- If this was the first composition for a new workspace: "First `/compose` run for [workspace]. The voice kernel will grow as we run more compositions and capture corrections."

---

## Success Criteria

- [ ] Approved draft delivered via the format's mechanism
- [ ] Operator confirmed receipt
- [ ] Delivery summary provided

---

*End of workflow. For the next composition, invoke `/compose` again.*
