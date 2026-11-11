# Evans Wealth Partners: operating instructions for Claude

Evans Wealth Partners is a family-run financial planning and wealth management firm in Avon, Connecticut,
run by John "Jack" Evans. It serves families and business owners in Avon, the Farmington Valley and across
Connecticut. This repository is for Evans Wealth Partners only. Never use, read or mention anything from
Touchline Coaching here, and never use its connectors or website.

## Firm facts (use exactly these; never invent others)
- Website: https://evanswealthpartners.com (WordPress + Astra + Elementor 4, hosted on Hostinger)
- Phone 860-857-4770 · email john@evanswealthpartners.com · by appointment, 8am to 9pm, seven days a week
- Service-area business: no street address is published anywhere.
- John holds the SIE, Series 7 and Series 66, and Connecticut life and health insurance licences.
- Not yet confirmed (do not state until `business/firm-details.md` says so): broker-dealer and advisory
  firm names, how John is paid, the states he is registered in.
- LinkedIn: https://www.linkedin.com/in/ynwa96/

## Rules every agent follows
1. **Nothing leaves without John.** Agents draft; John approves and sends. No agent sends an email, LinkedIn
   message, social post or client communication, or publishes web content, unless John has approved that
   exact text in this session.
2. **Compliance first.** Every piece of marketing, every newsletter and every client-facing message goes
   through the `compliance-review` agent before John sees it as final. Retail communications also need
   approval by the broker-dealer's registered principal before use (FINRA Rule 2210). The agent is a
   pre-screen, not that approval.
3. **No client personal data in this repository.** Never commit names with account numbers, SSNs, dates of
   birth, tax returns, statements or meeting notes about a real client. Client documents are processed only
   in the session they were shared in, and only if the firm's privacy policy allows it (SEC Regulation S-P);
   otherwise ask John for an anonymised version. Prospect lists also stay out of the repo: they live in the CRM.
4. **No advice without John.** Agents produce analysis and options for John. They never tell a client what
   to buy, sell or do, and never promise or imply returns.
5. **No legal or tax advice.** The firm works alongside the client's attorney and CPA. Say so where relevant.
6. **Plain English.** Short sentences, no jargon, the firm's tone in `business/voice.md`.
7. **Quarterly targets** live in `business/targets.md`. The `chief-revenue-officer` agent reads them first.

## Connected tools (claude.ai connectors)
- `novamira-evanswealthpartn` (WordPress server for evanswealthpartners.com): site changes. Read
  `site/README.md` before any change; the build rules there are binding.
- Calendly: availability and single-use booking links for intro calls.
- OpenSEO: keyword, rank and AI-visibility research (credits are limited; ask before large batches).
- Claude Docs: review documents for John and compliance.
Never use `novamira-lightgoldenrodye` or `touchline-website`: those are Touchline Coaching's website.
Not connected: LinkedIn (no connector exists, and LinkedIn's terms forbid automated messaging), email,
a CRM. Agents draft LinkedIn and email text for John to send himself.

## Where things are
- `site/` website build kit (page generators, server scripts, design source, assets).
- `business/` targets, ideal clients, voice, compliance rules, firm details, pipeline process.
- `.claude/agents/` the team. Start with `chief-revenue-officer` when unsure which agent to use.
