---
name: process-guardian
description: "Quality gate for all AI Business Builder outputs. Scores deliverables on a 10-point checklist covering specificity, phase alignment, quality, and completeness. Auto-revises outputs scoring 7-8, rewrites those below 7. Use this skill whenever reviewing or validating any output from the business builder agents."
---

# Process Guardian Scoring Checklist

## 10-Point Scoring System

### Specificity (3 points)
1. **Business-specific** - Tailored to user's actual business, not generic
2. **Actionable details** - Includes specific numbers, dates, templates, scripts
3. **Ready to use** - User can execute immediately without additional work

### Phase Alignment (2 points)
4. **Correct phase** - Matches user's actual stage
5. **Right scope** - Appropriate scale (MVPs are minimal, research is focused)

### Quality (3 points)
6. **No AI slop** - No em dashes, "leverage", "seamless", corporate jargon
7. **Natural voice** - Human-written feel
8. **Evidence-based** - Supported by research or customer data

### Completeness (2 points)
9. **Full deliverable** - No placeholders or "insert here" sections
10. **Clear next step** - User knows what to do after reading

## Scoring Actions
- 9-10: APPROVED
- 7-8: AUTO-REVISE (fix and re-score)
- Below 7: REWRITE

## Instant Fails
- Placeholder text present
- Wrong phase advice
- Fabricated research
- MVP with 4+ features
- Non-pasteable prompts
