---
name: build-flow
description: "Orchestrates Phase 3 (Build MVP) end-to-end. Creates a lean PRD focused on ONE feature, generates a ready-to-paste prompt for AI coding platforms, and enforces the one-week shipping deadline. Use when someone has a validated offer and needs to build the minimum viable product."
---

# Build Flow

Orchestrates Phase 3 using prd-writer and prompt-engineer.

## Prerequisites
- Completed Phase 2 (landing page live, outreach started)
- Customer feedback from outreach conversations
- If no landing page or outreach yet, route back to launch-flow

## Sequence

```
1. Identify the ONE core feature (ask user, push back on scope creep)
2. prd-writer: Lean PRD with user flow, design, and explicit out-of-scope list
   -> process-guardian reviews (must have <3 features, out-of-scope section)
3. prompt-engineer: Convert PRD into builder prompt
   -> process-guardian reviews (must be copy-pasteable)
4. User builds MVP in AI coding platform
5. Ship within one week
```

## Marty Cagan's 5 MVP Questions

Before building, the MVP must have a credible answer for each of these (from Marty Cagan, via Yuval Samet / RiseUp):

1. **Can they use it?** (Usability) - Will users actually understand how to use it without hand-holding?
2. **Would they use it?** (Value) - Is there enough value that they'd come back and recommend it?
3. **Can we build it?** (Technical Feasibility) - Can this scale beyond a prototype? If you're doing everything manually and saying "we'll automate later" with no plan, that's not MVP, that's Wishful Thinking.
4. **Is it financially viable?** (Unit Economics) - Does the math work at scale? Can you deliver this without losing money per customer?
5. **Should we do it?** (Ethics) - Is the business model ethical? Are you exploiting user data or creating genuine value?

You don't need perfect answers. But you need a credible hypothesis for each, especially #3 (technical feasibility).

## The ONE Feature Test

Before the PRD starts, force this question:

> "If you could only ship ONE feature and nothing else, what would it be? That's your MVP."

Examples of right-sized MVPs:
- Outreach tool: "build a prospect list" (not the full pipeline)
- Content tool: "repurpose one post" (not a content calendar)
- Analytics tool: "one dashboard view" (not a reporting suite)
- PR tool: "generate one reporter brief" (not media monitoring)

If the user lists more than one feature, pick the one closest to the core value and defer everything else to v2.

## Phase 3 Checklist

Before moving to Phase 4, verify:
- [ ] MVP is live and accessible
- [ ] Core feature works end-to-end
- [ ] At least 3 people have tried it
- [ ] Build took one week or less
- [ ] "Out of scope" features are documented for later

## Not Everything Is an App

Your AI business could be a totally different idea that doesn't require building an app. It could be a service, a workflow, a consulting package, a template library. Just figure out the quickest way to deliver a first version of the product to customers.

If the MVP is not software:
- Skip the PRD and builder prompt steps
- Instead: define the deliverable, the process to produce it, and how to deliver it
- Ship within one week regardless
- The ONE Feature Test still applies: what's the one thing you deliver?

## Common Mistakes to Flag
- Building 5+ features before anyone pays
- Spending time on auth, settings, admin panels before core value works
- Choosing complex tech when a simple tool would do
- Iterating on design instead of shipping
- Not showing the MVP to anyone until it's "ready"
- **The Bond mistake:** Building too much before going to market, then realizing customers wanted something different, forcing a complete rebuild. This cost months and real money.
- **The Wishful Thinking trap:** Building a 100% manual/human service and saying "we'll automate later." If you have no hypothesis for how to scale it technically, you don't have an MVP, you have a consulting gig. (Yuval Samet, RiseUp)
- **Giving it away free and calling it validated.** Pricing is a feature of the product. Until people pay, you haven't validated. (See Phase 4)

## Failure Modes
- **Taking longer than 1 week:** You're building too much. Cut features ruthlessly.
- **User wants to add "just one more thing":** That's scope creep. Ship what you have. Add later.
- **MVP doesn't solve the problem:** That's OK — you learned fast. Go back to the offer and iterate.

## Quality Gates
- [ ] ONE core feature, nothing more
- [ ] Build took one week or less
- [ ] MVP is live and accessible to real users
- [ ] Out-of-scope list is documented
- [ ] At least 3 people have tried it
- [ ] Builder prompt was copy-pasteable (no editing needed)

## Handoff
When MVP is live and tested, route to monetize-flow (Phase 4).
