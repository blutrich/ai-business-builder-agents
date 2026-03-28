# AI Business Builder - Agent System One-Pager

## What Is This?

A Claude Code plugin that coaches non-technical founders through building an AI-powered business from idea to scale. It's not a chatbot that gives advice - it's a multi-agent system that produces deliverables: research reports, interview questionnaires, landing page copy, PRDs, outreach campaigns, pricing strategies, and growth plans.

Built from the real experience of building Bond, a $5M AI business in 12 months. The most expensive lesson: building too much before validating. This system exists so you don't make that mistake. Additional MVP wisdom from Yuval Samet (RiseUp co-founder/CPO) and Marty Cagan's product validation framework.

## How It Works

A user describes where they are. The **Business Router** diagnoses their phase and routes them to the right specialist agents. Every output passes through the **Process Guardian** (quality gate) before reaching the user.

```
User -> Business Router -> Phase Flow -> Specialist Agents -> Process Guardian -> Deliverable
```

## The 5 Phases

| Phase | Goal | Key Rule |
|-------|------|----------|
| **1. Validation** | Find a problem worth solving | Research 2hrs max, then 9 customer interviews. Don't pitch. |
| **2. Launch** | Turn the idea into an offer | Offer before product. Direct response copy. Domain first. |
| **3. Build MVP** | Ship the minimum | ONE feature. ONE week. Pass Cagan's 5 questions. |
| **4. Monetize** | Get people to pay | Pricing is a feature. 5 new strangers (not friends). 50% early discount. |
| **5. Growth** | Scale what works | Outreach > Organic > Retargeting. Automate manually-proven only. |

## The 8 Specialist Agents

| Agent | Model | What It Does | Framework |
|-------|-------|-------------|-----------|
| **research-agent** | Sonnet | Finds real pain on Reddit/forums | Pain signal detection |
| **interview-agent** | Sonnet | Generates questionnaires, analyzes transcripts | Torres Opportunity Tree |
| **offer-architect** | Opus | Creates irresistible offers + landing page copy | Hormozi Value Equation |
| **brand-builder** | Sonnet | Domain strategy, branding, design direction | Domain-first approach |
| **prompt-engineer** | Opus | Copy-paste prompts for AI coding platforms | Meta-prompt generation |
| **prd-writer** | Opus | Lean PRDs with feasibility check | ONE Feature + Cagan's 5 Qs |
| **monetization-strategist** | Opus | Pricing, business model, outreach sequences | Revenue Gate + pricing-as-feature |
| **growth-strategist** | Opus | Growth Trifecta + automation roadmap | Product-Channel Fit |

## The Process Guardian

Every deliverable gets scored on a 10-point checklist:

- **Specificity** (3pts): Business-specific? Actionable? Ready to use?
- **Phase Alignment** (2pts): Right phase? Right scope?
- **Quality** (3pts): No AI slop? Natural voice? Evidence-based?
- **Completeness** (2pts): No placeholders? Clear next step?

**9-10/10:** Ships as-is. **7-8/10:** Auto-revised. **Below 7/10:** Rewritten.

**Instant fails:** Placeholder text, wrong-phase advice, fabricated research, MVP with 4+ features, Wishful Thinking (100% manual with no automation path).

## Key Frameworks

**Torres Opportunity Solution Tree** (Phase 1) - Map the problem space before committing to a solution. Explore 3 opportunities, validate through interviews, prune dead branches.

**Hormozi Value Equation** (Phase 2) - Value = (Dream Outcome x Perceived Likelihood) / (Time Delay x Effort). Build an offer stack: core + bonuses + guarantee + scarcity.

**The ONE Feature Test** (Phase 3) - "If you could only ship ONE feature, what would it be?" Build that. Nothing else.

**Marty Cagan's 5 MVP Questions** (Phase 3) - Before building, answer:
1. Can they use it? (Usability)
2. Would they use it? (Value)
3. Can we build it? (Technical Feasibility - "we'll automate later" without a plan = Wishful Thinking)
4. Is it financially viable? (Unit Economics)
5. Should we do it? (Ethics)

**The Revenue Gate** (Phase 4) - Pricing is a feature of the product. Free users don't validate willingness to pay. 5 paying strangers for B2B, 50-100 for consumer. If you can't get them after 30 days, the problem is the offer.

**The Growth Trifecta** (Phase 5) - Personalized outreach (Month 1) + Organic content (Month 2-3) + Paid retargeting (Month 3-4). Build in sequence, not simultaneously.

## What Makes This Different

1. **Phase discipline** - Won't let you skip ahead. Most founders build too early. This system catches that.
2. **Real deliverables** - Not advice. Actual copy-pasteable outputs you can use today.
3. **Quality gate on everything** - The Process Guardian catches generic advice, AI slop, scope creep, and Wishful Thinking.
4. **Tool agnostic** - Suggests categories (AI builders, outreach tools, note-takers) with 2-3 examples. Never mandates one tool.
5. **Battle-tested** - Every rule comes from a real mistake that cost real money at Bond.
6. **Feasibility-aware** - Flags MVPs that are 100% manual with no automation path. Pricing validation is baked in from day one.

## Eval Results

6 evals covering all 5 phases + edge cases (phase skipping, weak PMF detection):

- **With skill: 100%** (31/31 assertions passed)
- **Without skill: 32.4%** (11/34 passed)
- **Delta: +67.6 percentage points**

The biggest win: when a user tries to skip from research straight to coding, the skill catches the phase skip and redirects. Without the skill, Claude happily provides a full tech stack.

## Architecture

```
plugins/ai-business-builder/
  agents/           8 specialists + shared instructions + process guardian
  skills/           7 flow skills (router + guardian + 5 phases)
  scripts/          3 Python scripts (Reddit, competitors, LinkedIn)
  brands/           Quality standards + anti-patterns
  references/       Source transcripts (Ofer's Bond framework, Yuval Samet MVP podcast)
```

**Architecture Diagram:** [Excalidraw](https://excalidraw.com/#json=lHXMZK8qC_cG3VMzO9Gn0,YvjNdsNTzEfoagC6qBVb-Q)

## Sources

- **Ofer Blutrich** - Bond ($5M AI business) framework: 5 phases, validation-first, revenue gate
- **Yuval Samet** (RiseUp) - MVP validation: pricing-as-feature, 50-100 customer benchmark, Wishful Thinking anti-pattern
- **Marty Cagan** - 5 MVP questions: usability, value, feasibility, unit economics, ethics

---

*Built by Ofer Blutrich. MIT License.*
