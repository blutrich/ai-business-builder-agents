---
name: launch-flow
description: "Orchestrates Phase 2 (Launch) end-to-end. Creates an irresistible offer using the Hormozi framework, builds branding, generates landing page copy, and produces a ready-to-paste prompt for AI coding platforms. Use when someone has a validated idea and needs to get it in front of people fast."
---

# Launch Flow

Orchestrates Phase 2 using offer-architect, brand-builder, and prompt-engineer.

## Prerequisites
- Completed Phase 1 (validated problem, target customer identified)
- If not validated, route back to validation-flow

## Sequence

```
1. brand-builder: Domain + branding
   -> Start with domain, not name (domains are harder to find)
   -> Go for .com, .io, or .ai
   -> Try prefixes/suffixes if taken: get[name], go[name], ask[name], try[name]
   -> Aim for ~$11 range, skip anything over $50 at this stage
   -> Logo: Upwork/Fiverr or AI image generation tools
   -> process-guardian reviews

2. offer-architect: Irresistible offer + landing page copy
   -> Describe the product, the problem, and who it's for
   -> Ask to write it "like a direct response marketer" (copywriters who specialize in getting people to take action)
   -> Sell the OUTCOME, not the product. Sales is selling someone on an outcome. The product is just how they receive that outcome.
   -> process-guardian reviews

3. prompt-engineer: Convert to ready-to-paste builder prompt
   -> Include: design style, color scheme, dark/light mode preferences
   -> Include: all the landing page copy from step 2
   -> The prompt must work in AI coding platforms (Lovable, Base44, Bolt, v0, Replit, or similar)
   -> process-guardian reviews

4. Design refinement (optional but recommended):
   -> Get design inspiration from template galleries (Webflow templates, Framer templates, Dribbble)
   -> Screenshot sections of websites you like
   -> Upload screenshots to the AI builder with: "Copy the design system from these screenshots, including the color usage, fonts, tone, and everything from this brand book"

5. User publishes landing page and gets a live URL
   -> Connect domain to the published site
   -> Share the link immediately

6. Start outreach immediately (in parallel with Phase 3)
```

## Phase 2 Checklist

Before moving to Phase 3, verify:
- [ ] Domain purchased (~$11, not expensive)
- [ ] Landing page live with a real URL
- [ ] Offer copy sells the outcome, not the product
- [ ] Written like a direct response marketer (conversion-focused)
- [ ] CTA is clear (waitlist, free trial, demo, or buy)
- [ ] At least 10 people have seen the page
- [ ] Outreach started (even if just 5-10 messages)

## Common Mistakes to Flag
- Spending more than 3 days on the landing page
- Choosing an expensive domain ($100+) at this stage
- Starting with a name instead of a domain (domain is harder to find)
- Writing feature-focused copy instead of outcome-focused
- Waiting until the page is "perfect" before sharing it
- Not starting outreach in parallel

## Failure Modes
- **Can't find a good domain:** Use prefixes (get, go, ask, try) or try .ai extension. Don't let this block you.
- **Landing page doesn't convert:** The problem is the offer, not the design. Revisit copy first.
- **No responses to outreach:** Fine-tune the offer based on what you're hearing in conversations.

## Quality Gates
- [ ] Domain purchased and connected
- [ ] Landing page is live with real URL
- [ ] Copy is conversion-focused (direct response style)
- [ ] Builder prompt is copy-pasteable
- [ ] Outreach has started in parallel

## Handoff
When all checklist items are done, route to build-flow (Phase 3).
