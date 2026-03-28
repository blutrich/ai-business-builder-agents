# AI Business Builder Agents

A multi-agent plugin for Claude Code that helps non-technical founders build AI-powered businesses from idea to scale. Think of it as an AI company that works for you: 8 specialist agents, 1 lead orchestrator, 1 process guardian, 5 phase orchestration flows, and 3 built-in scrapers.

This isn't a chatbot that gives advice. It's a system that produces deliverables: research reports, customer interview questionnaires, landing page copy, ready-to-paste coding prompts, PRDs, pricing strategies, outreach campaigns, growth plans, and more.

## Architecture

```
User
  |
  v
business-router (Lead Orchestrator)
  |
  |-- Phase Detection (where are you?)
  |-- Agent Routing (who should do the work?)
  |-- Process Guardian (quality gate on every output)
  |
  v
Phase Flow Skills (orchestrate each phase end-to-end)
  |
  |-- validation-flow   Phase 1: Torres Opportunity Tree + research + interviews
  |-- launch-flow       Phase 2: Hormozi offer + branding + landing page
  |-- build-flow        Phase 3: ONE feature MVP + one-week deadline
  |-- monetize-flow     Phase 4: First 5 customers + revenue gate
  |-- growth-flow       Phase 5: Growth Trifecta + automation
  |
  v
Specialist Agents (do the actual work)
  |
  |-- research-agent        Scrapes forums/Reddit for pain points
  |-- interview-agent       Generates questionnaires, analyzes transcripts
  |-- offer-architect       Hormozi irresistible offer + landing page copy
  |-- brand-builder         Domain, branding, design direction
  |-- prompt-engineer       Ready-to-paste prompts for AI builders
  |-- prd-writer            Lean PRDs for MVP builds
  |-- monetization-strategist  Pricing, business model, first 5 customers
  |-- growth-strategist     Growth trifecta + automation roadmap
  |
  v
process-guardian (Quality Gate)
  |
  |-- 10-point scoring checklist
  |-- Auto-revise (7-8/10) or rewrite (<7/10)
  |-- Phase-specific validation rules
  |-- Pattern logging for continuous improvement
```

## The 5 Phases

### Phase 1: Validation
**Flow:** validation-flow
**Agents:** research-agent, interview-agent
**Framework:** Torres Opportunity Solution Tree

The validation flow maps the opportunity space before diving into research. It builds an Opportunity Solution Tree:

```
            [DESIRED OUTCOME]
                  |
      -------------------------
      |           |           |
[Opportunity A] [Opportunity B] [Opportunity C]
      |           |           |
   -------     -------     -------
   |     |     |     |     |     |
 [Sol] [Sol] [Sol] [Sol] [Sol] [Sol]
```

**Deliverables:**
- Opportunity Solution Tree mapping the problem space
- Problem research report with real quotes from Reddit/forums/Twitter
- Customer discovery questionnaire tailored to your business
- Interview transcript analysis with segment recommendations
- Validated opportunity with evidence

### Phase 2: Launch
**Flow:** launch-flow
**Agents:** offer-architect, brand-builder, prompt-engineer
**Framework:** Hormozi Irresistible Offer (B2B + B2C specific)

The offer-architect uses the Hormozi Value Equation:
```
Value = (Dream Outcome x Perceived Likelihood) / (Time Delay x Effort)
```

With specific adaptations for B2B (ROI-focused, demo CTA, integration objections) and B2C (emotion-focused, instant access, identity-driven).

**Deliverables:**
- Irresistible offer with offer stack (core + bonuses + guarantee + scarcity)
- Full landing page copy written as direct response marketing
- Brand brief with domain suggestions, colors, typography
- Ready-to-paste prompt for AI coding platforms

### Phase 3: Build MVP
**Flow:** build-flow
**Agents:** prd-writer, prompt-engineer

Enforces the ONE Feature Test: "If you could only ship ONE feature, what would it be?"

**Deliverables:**
- Lean PRD focused on ONE core feature
- App builder prompt ready to paste
- Explicit "out of scope" list to prevent overbuilding
- One-week shipping deadline

### Phase 4: Monetization
**Flow:** monetize-flow
**Agents:** monetization-strategist

Enforces the Revenue Gate: 5 paying customers (not friends, not free users).

**Deliverables:**
- Business model recommendation (SaaS, usage-based, freemium, etc.)
- Specific pricing with early adopter discount
- "First 5 Customers" plan with outreach sequences
- Closing scripts and qualification criteria

### Phase 5: Growth
**Flow:** growth-flow
**Agents:** growth-strategist

Builds the Growth Trifecta in sequence (not simultaneously):

**Deliverables:**
- Outreach at scale blueprint (Month 1)
- 4-week organic content calendar (Month 2-3)
- Retargeting strategy with budget allocation (Month 3-4)
- Automation roadmap prioritized by time saved

## Process Guardian

Every output passes through the process-guardian before reaching you.

**10-Point Scoring:**
- Specificity (3pts): Business-specific? Actionable? Ready to use?
- Phase Alignment (2pts): Correct phase? Right scope?
- Quality (3pts): No AI slop? Natural voice? Evidence-based?
- Completeness (2pts): No placeholders? Clear next step?

**Scoring Actions:**
- 9-10/10: Approved. Ships as-is.
- 7-8/10: Auto-revised. Fixes applied, re-scored.
- Below 7/10: Rewritten from scratch.

**Instant fails:** placeholder text, wrong phase advice, fabricated research, MVP with 4+ features, non-pasteable prompts.

## Built-in Scripts

The plugin includes Python scripts that agents can use for research and growth:

| Script | Phase | What It Does |
|--------|-------|-------------|
| `reddit_scraper.py` | 1 | Searches Reddit for pain points, detects frustration signals, generates research reports |
| `competitor_scanner.py` | 1 | Maps competitive landscape from Reddit discussions, extracts competitor names |
| `linkedin_engagers.py` | 5 | Generates outreach plans and message templates for LinkedIn post engagers (plan generator, not extractor — use a prospecting tool like Bond/Phantombuster to extract engagers first) |

**All scripts use Python stdlib only (no pip install needed).**

Usage examples:
```bash
# Research pain points
python scripts/reddit_scraper.py "outbound sales" --subreddits sales,startups --limit 50

# Map competitors
python scripts/competitor_scanner.py "AI writing tools" --output report.md

# Plan engager outreach
python scripts/linkedin_engagers.py "https://linkedin.com/posts/..." --output plan.md
```

## Installation

### As a Claude Code Plugin

```bash
# Clone the repo
git clone https://github.com/blutrich/ai-business-builder-agents.git

# Copy or symlink to your Claude Code plugins path
cp -r ai-business-builder-agents/plugins/ai-business-builder ~/.claude/plugins/ai-business-builder
```

Or with a symlink:
```bash
git clone https://github.com/blutrich/ai-business-builder-agents.git ~/projects/ai-business-builder-agents
ln -s ~/projects/ai-business-builder-agents/plugins/ai-business-builder ~/.claude/plugins/ai-business-builder
```

### Manual Installation

1. Copy the `plugins/ai-business-builder/` directory to `~/.claude/plugins/ai-business-builder/`
2. Restart Claude Code
3. The `business-router` skill will appear in your available skills

## Usage

Just describe where you are. The router figures out the rest.

**Starting from scratch:**
> "I have an idea for an AI tool that helps recruiters screen resumes faster. Where do I start?"

**Have an MVP, need customers:**
> "I built a prototype but nobody's paying. What do I do?"

**Have revenue, need growth:**
> "I'm making $5k/month from 15 customers. How do I 10x this?"

**Need a specific deliverable:**
> "Write me a landing page for my AI scheduling tool"
> "Create a PRD for my MVP"
> "Give me outreach messages for my first 5 customers"

## Key Frameworks

### Torres Opportunity Solution Tree (Phase 1)
Map opportunities before committing to a solution. Explore 3 opportunities, generate 2-3 solutions each, validate the strongest through customer interviews, prune dead branches.

### Hormozi Irresistible Offer (Phase 2)
```
Value = (Dream Outcome x Perceived Likelihood) / (Time Delay x Effort)
```
Build an offer stack: core product + acceleration bonus + risk-reduction bonus + effort-removal bonus + scarcity.

### The MVP Rule (Phase 3)
If you could only ship ONE feature, what would it be? Build that. Nothing else. Ship in one week.

### The Revenue Gate (Phase 4)
5 paying customers who are NOT friends or family. If you can't get 5 to pay after 30 days, the problem is the offer, not the product.

### The Growth Trifecta (Phase 5)
Personalized outreach (Month 1) + Organic content (Month 2-3) + Paid retargeting (Month 3-4) = Compounding growth engine. Build in sequence, not simultaneously.

## Agent Details

Each agent is built around a specific framework or principle from the real experience of building Bond ($5M AI business). They're not generic assistants - they encode hard-won lessons about what actually works at each stage.

| Agent | Model | Phase | What It Produces |
|-------|-------|-------|-----------------|
| research-agent | Sonnet | 1 | Research reports with real forum quotes |
| interview-agent | Sonnet | 1 | Questionnaires + transcript analysis |
| offer-architect | Opus | 2 | Hormozi offers + landing page copy (B2B/B2C) |
| brand-builder | Sonnet | 2 | Domain suggestions + brand briefs |
| prompt-engineer | Opus | 2,3 | Copy-paste prompts for AI builders |
| prd-writer | Opus | 3 | Lean PRDs for one-feature MVPs |
| monetization-strategist | Opus | 4 | Pricing + outreach + closing scripts |
| growth-strategist | Opus | 5 | Growth trifecta + automation plans |
| process-guardian | Opus | All | 10-point quality scoring + auto-revision |
| business-router | - | All | Lead orchestrator, phase detection |

### The Thinking Behind Each Agent

**research-agent** (Sonnet) - The whole point of Phase 1 is finding real people expressing real frustration. Not market sizing, not industry reports. This agent searches Reddit, forums, and communities for specific quotes and pain signals. It uses Sonnet because the task is structured data gathering, not strategic reasoning. The key insight: if you can't find people complaining about the problem, the problem might not be worth solving.

**interview-agent** (Sonnet) - Research shows a problem exists. Interviews tell you if YOUR approach resonates. This agent generates customer discovery questionnaires and analyzes transcripts. It enforces the cardinal rule: do NOT talk about your product during interviews. It also handles the multi-segment approach (3 groups x 3 people = 9 interviews) that prevents you from chasing the wrong customer.

**offer-architect** (Opus) - Built around the Hormozi Value Equation: Value = (Dream Outcome x Perceived Likelihood) / (Time Delay x Effort). This agent turns a validated problem into an irresistible offer with specific adaptations for B2B (ROI-focused, demo CTA) and B2C (emotion-focused, instant access). It writes like a direct response marketer because the landing page copy needs to convert, not just inform. Uses Opus because strategic positioning requires complex reasoning across multiple frameworks.

**brand-builder** (Sonnet) - The real lesson from Bond: start with the domain, not the name. Domains are harder to find. This agent suggests .com, .io, .ai options with prefix strategies (get, go, ask, try) and keeps costs around $11 - no $500 vanity domains at this stage. It also pulls design inspiration from template galleries (Webflow, Framer) so the landing page looks professional without hiring a designer.

**prompt-engineer** (Opus) - The bridge between strategy and execution. Non-technical founders need to paste a prompt into an AI coding platform (Lovable, Base44, Bolt) and get something usable on the first try. This agent produces four types of prompts: landing pages, MVP apps, research queries, and design clones. Uses Opus because generating effective prompts requires meta-reasoning about how AI models interpret instructions - you're essentially writing code that writes code.

**prd-writer** (Opus) - Enforces the most expensive lesson from Bond: they built too much before going to market, then realized customers wanted something different, forcing a complete rebuild. This agent creates lean PRDs focused on ONE feature. It explicitly skips the tech stack (let the builder choose) and includes an "out of scope" section to prevent scope creep. The one-week shipping deadline is non-negotiable. Uses Opus because deciding what NOT to build requires strategic judgment.

**monetization-strategist** (Opus) - Until there's a dollar in the bank, you have a money hole, not a business. This agent drives toward the Revenue Gate: 5 paying customers who are NOT friends or family. It selects from business models (SaaS, usage-based, freemium, etc.), sets specific pricing with 50% early adopter discounts, and creates outreach sequences. It also enforces the anti-pattern: don't invest in SEO, YouTube, or content marketing at this stage - those take 6-12 months. Direct outreach is the fastest feedback loop.

**growth-strategist** (Opus) - Once monetization works, everything changes. This agent builds the Growth Trifecta in sequence (not simultaneously): (1) personalized outreach at scale, (2) organic content (especially LinkedIn for B2B), (3) paid retargeting of warm audiences. The key insight from Bond: people who engage with your LinkedIn posts are 3-5x more likely to respond to outreach. Extract engagers, qualify them, do personalized outreach. For automation, the rule is: only automate things that work manually first.

**process-guardian** (Opus) - Every deliverable passes through this quality gate before reaching the user. It uses a 10-point scoring checklist covering specificity (is this tailored to their business?), phase alignment (right advice for where they are?), quality (no AI slop?), and completeness (no placeholders?). Score 9-10 ships as-is, 7-8 gets auto-revised, below 7 gets rewritten. Instant fails: placeholder text, wrong-phase advice, fabricated research, MVPs with 4+ features. Uses Opus because quality judgment requires understanding all 5 phases and detecting subtle issues.

**business-router** (Lead Orchestrator) - The entry point. Diagnoses which phase the user is in by asking a few quick questions, then routes to the right flow and agents. It never dumps all 5 phases at once. The coaching approach: diagnose first, coach the current phase, flag mistakes before they happen, push them to the next phase. Most people stay too long in Build - the router pushes them toward Monetization as fast as possible.

## Skill Details

| Skill | Phase | What It Orchestrates |
|-------|-------|---------------------|
| business-router | All | Entry point, phase diagnosis, agent routing |
| process-guardian | All | Quality gate scoring checklist |
| validation-flow | 1 | Torres tree + research + interviews |
| launch-flow | 2 | Hormozi offer + branding + landing page prompt |
| build-flow | 3 | ONE feature PRD + builder prompt + one-week deadline |
| monetize-flow | 4 | Business model + pricing + first 5 customers plan |
| growth-flow | 5 | Growth Trifecta + automation roadmap |

## Tool Philosophy

This plugin is tool-agnostic. Agents suggest categories with 2-3 examples:

| Category | Suggestions |
|----------|------------|
| AI Assistants | ChatGPT, Claude, Gemini, Perplexity |
| AI Coding Platforms | Lovable, Base44, Bolt, Replit, v0 |
| Note-takers | Fireflies, Otter, Fathom, tl;dv |
| Outreach Tools | Apollo, Instantly, Lemlist, Clay |
| Ad Platforms | Meta Ads, Google Ads, LinkedIn Ads |
| Automation | Make, Zapier, n8n |
| CRM | HubSpot, Pipedrive |
| Domain Registrars | Namecheap, Porkbun, GoDaddy |
| Design Inspiration | Webflow templates, Framer, Dribbble |

## File Structure

```
plugins/ai-business-builder/
  agents/
    shared-instructions.md    # Common rules for all agents
    research-agent.md         # Phase 1: Pain point research
    interview-agent.md        # Phase 1: Customer discovery
    offer-architect.md        # Phase 2: Hormozi offers (B2B/B2C)
    brand-builder.md          # Phase 2: Domain + branding
    prompt-engineer.md        # Phase 2+3: Builder prompts
    prd-writer.md             # Phase 3: Lean PRDs
    monetization-strategist.md # Phase 4: Revenue strategy
    growth-strategist.md      # Phase 5: Growth engine
    process-guardian.md       # Quality gate
  skills/
    business-router/SKILL.md  # Lead orchestrator
    process-guardian/SKILL.md  # Scoring checklist
    validation-flow/SKILL.md  # Phase 1 orchestration
    launch-flow/SKILL.md      # Phase 2 orchestration
    build-flow/SKILL.md       # Phase 3 orchestration
    monetize-flow/SKILL.md    # Phase 4 orchestration
    growth-flow/SKILL.md      # Phase 5 orchestration
  scripts/
    reddit_scraper.py         # Reddit pain point research
    competitor_scanner.py     # Competitive landscape mapping
    linkedin_engagers.py      # Post engager outreach planning
  brands/
    defaults/RULES.md         # Quality standards + anti-patterns
  plugin.json                 # Plugin manifest
```

## Origin

This framework comes from building a $5M AI business (Bond) in 12 months. The most expensive lesson: building too much before validating. This agent system exists so you don't make that mistake.

Built by Ofer Blutrich.

## License

MIT
