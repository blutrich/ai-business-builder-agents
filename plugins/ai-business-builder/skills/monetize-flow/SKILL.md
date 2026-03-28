---
name: monetize-flow
description: "Orchestrates Phase 4 (Monetization) end-to-end. Selects a business model, sets pricing, creates outreach campaigns, and drives toward the first 5 paying customers. Use when someone has a working MVP but no revenue yet."
---

# Monetize Flow

Orchestrates Phase 4 using monetization-strategist.

## Prerequisites
- Completed Phase 3 (working MVP, people have tried it)
- If no MVP, route back to build-flow
- If user is still building features, STOP them and route here

## Sequence

```
1. Verify MVP exists and has been tested by real people
2. monetization-strategist: Business model selection
   -> Choose from: subscription (SaaS), usage-based, marketplace, one-time purchase,
      freemium, service + software hybrid, or other (reference Dave Parker's 14 models)
   -> process-guardian reviews
3. monetization-strategist: Pricing + "First 5 Customers" outreach plan
   -> Set a starting price point
   -> Apply 50% early adopter discount for first customers
   -> Outreach sequences with specific, copy-pasteable messages
   -> process-guardian reviews
4. prompt-engineer: Generate outreach message prompts (if needed)
   -> process-guardian reviews
5. User executes outreach, closes first 5 customers
6. Collect feedback, iterate on product/pricing/targeting
```

## Key Rules (From Real Experience)

- **Don't charge old customers or friends.** Go find NEW paying customers through fresh outreach.
- **50% early adopter discount** on your starting price. This is your sales weapon early on.
- **Direct outreach is the #1 channel.** Personalized messaging campaigns are fastest for getting feedback.
- **Don't invest in slow channels yet.** SEO, content marketing, YouTube take 6-12 months to produce results. You need feedback NOW.
- **Paid ads CAN work** but targeting is harder early on. Stick to outreach first.
- **Be brutally honest** about what's not working. Don't be scared to change your product, who you're targeting, or the business model.
- When you find the right combo of customer + product + model, retention improves, referrals start, conversations get easier. That's product-market fit.
- **At product-market fit, consider:** Finding a technical co-founder, raising capital (VC route), or bootstrapping into growth.

## The Revenue Gate

This phase has ONE goal: get 5 people to pay.

Not 5 people to sign up. Not 5 people to say "cool idea." Five credit cards charged.

If the user can't get 5 people to pay after 30 days of outreach:
- The problem is the offer, not the product
- Revisit: Are you targeting the right people?
- Revisit: Is the price too high? Too low? (Too low signals no perceived value)
- Revisit: Does the MVP actually solve the problem?
- Consider pivoting the customer segment or the solution

## Phase 4 Checklist

Before moving to Phase 5, verify:
- [ ] 5+ paying customers (not friends/family)
- [ ] Clear business model chosen
- [ ] Price point tested and validated
- [ ] Outreach process is repeatable (not one-off hustle)
- [ ] Customer feedback collected from all 5
- [ ] Retention signal: are customers still using it after 2+ weeks?

## Common Mistakes to Flag
- Charging friends instead of finding real customers
- Giving it away free "to build a user base" (no. charge.)
- Adding features instead of selling what exists
- Investing in SEO/content before first dollar earned
- Setting price based on cost, not value delivered
- Not following up (most sales happen on follow-up 2-4)

## Failure Modes
- **Can't get 5 customers after 30 days:** The problem is the offer, not the product. Revisit targeting, pricing, or the value prop.
- **Customers sign up but churn fast:** The product doesn't solve the problem well enough. Go back to customer conversations.
- **Price resistance:** Try repositioning value (what outcome does it deliver?) before lowering price.

## Quality Gates
- [ ] 5+ paying customers (NOT friends or family)
- [ ] Clear business model chosen and documented
- [ ] Specific price point (not a range), with early adopter discount applied
- [ ] Outreach messages are personalized and copy-pasteable
- [ ] Customer feedback collected from all paying customers
- [ ] Retention signal: customers still using it after 2+ weeks

## Handoff
When 5+ paying customers exist and outreach is repeatable, route to growth-flow (Phase 5).
