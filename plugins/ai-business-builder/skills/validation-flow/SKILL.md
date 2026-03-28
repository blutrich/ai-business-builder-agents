---
name: validation-flow
description: "Orchestrates Phase 1 (Validation) end-to-end. Includes the Torres Opportunity Solution Tree for structured opportunity discovery. Use when someone needs to validate a business idea, explore opportunities, or map out the problem space before building."
---

# Validation Flow

Orchestrates the full validation process using the research-agent and interview-agent.

## Torres Opportunity Solution Tree

Before diving into research, structure the opportunity space using Teresa Torres' Opportunity Solution Tree framework. This prevents tunnel vision on a single solution.

### How to Build the Tree

```
                    [DESIRED OUTCOME]
                    (business goal)
                         |
            -------------------------
            |            |          |
      [Opportunity 1] [Opportunity 2] [Opportunity 3]
      (customer need)  (customer need) (customer need)
            |            |          |
         -------      -------    -------
         |     |      |     |    |     |
       [Sol] [Sol]  [Sol] [Sol] [Sol] [Sol]
```

### Step-by-Step

1. **Define the Desired Outcome** (top of tree)
   - What business result are you going after?
   - Example: "Help non-technical founders do outbound at scale"

2. **Map Opportunities** (middle layer)
   - These are customer needs/pain points discovered through research
   - Each opportunity is a different angle on the problem
   - Example:
     - Opportunity A: "Building targeted prospect lists takes too long"
     - Opportunity B: "Personalizing outreach at scale is impossible manually"
     - Opportunity C: "Existing tools are too expensive and complex"

3. **Generate Solutions** (bottom layer)
   - For each opportunity, brainstorm 2-3 possible solutions
   - These become potential MVPs to test
   - Example for Opportunity A:
     - Solution 1: AI-powered list builder from a description
     - Solution 2: Import from LinkedIn with auto-enrichment
     - Solution 3: Pre-built industry-specific prospect databases

4. **Prioritize**
   - Which opportunity has the strongest signal from research?
   - Which solution is fastest to build and test?
   - Pick ONE to validate through customer interviews

### Using the Tree with Agents

After research-agent produces the report:
1. Build the opportunity tree from the pain points discovered
2. Present the tree to the user
3. Let them pick which opportunity to explore
4. interview-agent creates questionnaires focused on that opportunity
5. After interviews, update the tree with what you learned
6. Prune dead branches (opportunities that didn't validate)
7. Double down on the strongest opportunity

## Critical Rules (From Real Experience)

### Research Phase
- **2 hours maximum.** This is light research to find real frustration, not industry analysis. The majority of time goes to customer interviews.
- Use any AI assistant (Claude, ChatGPT, Manus, Perplexity) to search forums, Reddit, Twitter for people complaining about the problem.
- Look for specific quotes and recurring frustrations, not abstract trends.
- What you're validating: (1) Who is the customer? (2) What problem are you solving? (3) Are people willing to pay?

### Customer Discovery Interviews
- **Do NOT talk about your product during the interview.** Tell them at the beginning that you'll share your idea at the end. The interview is about THEIR problems, not your solution.
- Book **15-minute video calls** (Zoom, Google Meet, etc.)
- Use an **AI note-taker** (Fireflies, Otter, Fathom, tl;dv, or similar) so you can focus on the conversation, not writing.
- If multiple customer segments might buy: **split into 3 groups, interview at least 3 per group** (9 total). You'll likely find 1-2 groups don't actually have the problem.
- **Stay very open.** Sometimes you stumble upon ideas that are way better to solve than what you initially went out to go after.
- After all interviews, **feed all transcripts to AI** and ask it to identify patterns, confirm whether the problem exists, and recommend which opportunity to pursue.

### Synthesis
- Feed ALL research notes + interview transcripts to an AI assistant.
- Ask: "Based on all of this, what problem should I solve, for whom, and why would they pay for it?"
- Use the answer to sharpen the idea before moving to Phase 2.

## Validation Flow Sequence

```
1. User describes idea
2. Build initial Opportunity Solution Tree (rough, from user's assumptions)
3. research-agent fills in evidence for each opportunity (2 hours max)
4. Update tree with research findings
5. User picks top 1-2 opportunities to validate
6. interview-agent creates targeted questionnaires
7. [User conducts 9 interviews: 3 segments x 3 people, 15 min each]
   CRITICAL: Do NOT pitch your product during interviews
8. interview-agent analyzes transcripts (fed through AI for pattern detection)
9. Update tree: prune weak branches, strengthen validated ones
10. Recommend: which opportunity + solution to build
11. Hand off to Phase 2 (Launch)
```

## Failure Modes

- **Research finds NO evidence of the problem:** Pivot the idea or explore adjacent problems. Don't force-fit.
- **Interviews contradict research:** Trust interviews over desk research. Real conversations beat forum posts.
- **Multiple segments seem viable:** Pick the one with the strongest pain signals and willingness to pay. You can always come back to the others.
- **Nobody seems willing to pay:** The problem may not be painful enough, or you're talking to the wrong people. Try a different segment before abandoning the idea.

## Quality Gates

- [ ] Research took < 2 hours
- [ ] At least 3 customer interviews completed (9 if multiple segments)
- [ ] No product pitching during interviews
- [ ] AI note-taker used for transcripts
- [ ] All transcripts fed to AI for pattern synthesis
- [ ] Clear problem statement supported by evidence
- [ ] Opportunity tree updated with validated/invalidated branches

## Output: The Validated Opportunity Tree

At the end of Phase 1, the user should have:

```
# Opportunity Solution Tree: [BUSINESS NAME]

## Desired Outcome
[What the business aims to achieve]

## Validated Opportunities (ranked)

### [Top Opportunity] - VALIDATED
- Evidence: [Research quotes + interview findings]
- Customer segments: [Who has this problem]
- Willingness to pay: [Strong/Moderate]
- Recommended solution: [The MVP to build]
- Why this one: [Summary of evidence]

### [Second Opportunity] - PARTIALLY VALIDATED
- Evidence: [What was found]
- Status: [Needs more interviews / Deprioritize / Pivot candidate]

### [Dead Branch] - NOT VALIDATED
- Why it failed: [What the research/interviews showed]
- Lesson: [What to remember]
```

This tree becomes the foundation for everything in Phase 2 and beyond.
