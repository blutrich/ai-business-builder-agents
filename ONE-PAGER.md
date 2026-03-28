# AI Business Builder - Agent System One-Pager

## What Is This?

A Claude Code plugin that coaches non-technical founders through building an AI-powered business from idea to scale. It's not a chatbot that gives advice - it's a multi-agent system that produces deliverables: research reports, interview questionnaires, landing page copy, PRDs, outreach campaigns, pricing strategies, and growth plans.

Built from the real experience of building Bond, a $5M AI business in 12 months. The most expensive lesson: building too much before validating. This system exists so you don't make that mistake.

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
| **3. Build MVP** | Ship the minimum | ONE feature. ONE week. Skip the tech stack. |
| **4. Monetize** | Get 5 people to pay | New customers, not friends. 50% early discount. No SEO yet. |
| **5. Growth** | Scale what works | Outreach > Organic > Retargeting. Automate manually-proven only. |

## The 8 Specialist Agents

| Agent | Model | What It Does | Framework |
|-------|-------|-------------|-----------|
| **research-agent** | Sonnet | Finds real pain on Reddit/forums | Pain signal detection |
| **interview-agent** | Sonnet | Generates questionnaires, analyzes transcripts | Torres Opportunity Tree |
| **offer-architect** | Opus | Creates irresistible offers + landing page copy | Hormozi Value Equation |
| **brand-builder** | Sonnet | Domain strategy, branding, design direction | Domain-first approach |
| **prompt-engineer** | Opus | Copy-paste prompts for AI coding platforms | Meta-prompt generation |
| **prd-writer** | Opus | Lean PRDs for one-feature MVPs | The ONE Feature Test |
| **monetization-strategist** | Opus | Pricing, business model, outreach sequences | The Revenue Gate |
| **growth-strategist** | Opus | Growth Trifecta + automation roadmap | Product-Channel Fit |

## The Process Guardian

Every deliverable gets scored on a 10-point checklist:

- **Specificity** (3pts): Business-specific? Actionable? Ready to use?
- **Phase Alignment** (2pts): Right phase? Right scope?
- **Quality** (3pts): No AI slop? Natural voice? Evidence-based?
- **Completeness** (2pts): No placeholders? Clear next step?

**9-10/10:** Ships as-is. **7-8/10:** Auto-revised. **Below 7/10:** Rewritten.

**Instant fails:** Placeholder text, wrong-phase advice, fabricated research, MVP with 4+ features.

## Key Frameworks

**Torres Opportunity Solution Tree** (Phase 1) - Map the problem space before committing to a solution. Explore 3 opportunities, validate through interviews, prune dead branches.

**Hormozi Value Equation** (Phase 2) - Value = (Dream Outcome x Perceived Likelihood) / (Time Delay x Effort). Build an offer stack: core + bonuses + guarantee + scarcity.

**The ONE Feature Test** (Phase 3) - "If you could only ship ONE feature, what would it be?" Build that. Nothing else.

**The Revenue Gate** (Phase 4) - 5 paying customers who are NOT friends or family. If you can't get 5 after 30 days, the problem is the offer.

**The Growth Trifecta** (Phase 5) - Personalized outreach (Month 1) + Organic content (Month 2-3) + Paid retargeting (Month 3-4). Build in sequence, not simultaneously.

## What Makes This Different

1. **Phase discipline** - Won't let you skip ahead. Most founders build too early. This system catches that.
2. **Real deliverables** - Not advice. Actual copy-pasteable outputs you can use today.
3. **Quality gate on everything** - The Process Guardian catches generic advice, AI slop, and scope creep.
4. **Tool agnostic** - Suggests categories (AI builders, outreach tools, note-takers) with 2-3 examples. Never mandates one tool.
5. **Battle-tested** - Every rule comes from a real mistake that cost real money at Bond.

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
```

**Architecture Diagram:** [Excalidraw](https://excalidraw.com/#json=zfgUzpllJ-OQPXgvsUkrO,eBhUVWj_FEIcjn29BQZAjQ)

---

*Built by Ofer Blutrich. MIT License.*
