#!/usr/bin/env python3
"""
Competitor & Alternative Scanner
Searches for competitors and alternatives in a problem space.
Used by the research-agent in Phase 1 to map the competitive landscape.

Usage:
    python competitor_scanner.py "AI outbound tools"
    python competitor_scanner.py "property description generator" --output report.md
"""

import argparse
import json
import sys
from urllib.request import urlopen, Request
from urllib.parse import quote_plus
from urllib.error import HTTPError


def search_alternatives(query: str) -> list[dict]:
    """Search for competitors/alternatives using Reddit and common patterns."""
    search_terms = [
        f"{query} alternative",
        f"{query} vs",
        f"best {query}",
        f"{query} comparison",
        f"{query} review",
    ]

    results = []
    for term in search_terms:
        url = f"https://www.reddit.com/search.json?q={quote_plus(term)}&sort=relevance&limit=10"
        headers = {"User-Agent": "AIBusinessBuilder/1.0"}
        req = Request(url, headers=headers)

        try:
            with urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode())
                for child in data.get("data", {}).get("children", []):
                    post = child.get("data", {})
                    results.append({
                        "title": post.get("title", ""),
                        "selftext": post.get("selftext", "")[:300],
                        "subreddit": post.get("subreddit", ""),
                        "score": post.get("score", 0),
                        "url": f"https://reddit.com{post.get('permalink', '')}",
                        "search_term": term,
                    })
        except Exception as e:
            print(f"Warning: Failed search for '{term}': {e}", file=sys.stderr)

    return results


def extract_competitor_names(results: list[dict]) -> list[str]:
    """Extract potential competitor names from search results."""
    # Common patterns that indicate a tool/product name
    import re

    all_text = " ".join(f"{r['title']} {r['selftext']}" for r in results)

    # Look for patterns like "I use X", "switched to X", "X is better"
    patterns = [
        r"(?:I use|we use|try|check out|switched to|moved to|using)\s+([A-Z][a-zA-Z0-9]+(?:\.[a-z]+)?)",
        r"([A-Z][a-zA-Z0-9]+(?:\.[a-z]+)?)\s+(?:is better|is great|works well|alternative)",
    ]

    names = set()
    for pattern in patterns:
        matches = re.findall(pattern, all_text)
        names.update(matches)

    # Filter out common English words
    stop_words = {"I", "The", "This", "That", "It", "We", "They", "My", "Our", "Your", "But", "And", "So", "If", "Not"}
    names = {n for n in names if n not in stop_words and len(n) > 2}

    return sorted(names)


def generate_report(query: str, results: list[dict], competitors: list[str]) -> str:
    """Generate competitive landscape report."""
    report = f"""# Competitive Landscape: "{query}"

## Potential Competitors Identified
{chr(10).join(f'- {name}' for name in competitors[:15]) if competitors else '- No specific competitors identified from Reddit data'}

## How People Talk About This Space

### Top Discussions
"""
    seen_titles = set()
    for r in sorted(results, key=lambda x: x["score"], reverse=True)[:15]:
        if r["title"] not in seen_titles:
            seen_titles.add(r["title"])
            report += f"""
**{r['title']}** (r/{r['subreddit']}, score: {r['score']})
> {r['selftext'][:200]}...
[Link]({r['url']})
"""

    report += """
## Analysis Framework

Use these questions to assess each competitor:

| Question | Why It Matters |
|----------|---------------|
| What do they charge? | Establishes price anchoring for your offer |
| What do users complain about? | Your opportunity to differentiate |
| What's their ideal customer? | Helps you find underserved segments |
| How complex is their product? | Simplicity can be your wedge |
| How long have they existed? | Newer = less lock-in for their users |

## Next Steps
1. Visit each competitor's website and note pricing, features, positioning
2. Read their G2/Capterra reviews (sort by lowest rating first)
3. Identify the gap: what are users asking for that nobody provides?
4. Use this gap as the foundation for your offer
"""
    return report


def main():
    parser = argparse.ArgumentParser(description="Scan for competitors in a problem space")
    parser.add_argument("query", help="Problem space to search (e.g., 'AI outbound tools')")
    parser.add_argument("--output", help="Output file path", default=None)
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    print(f"Scanning competitive landscape for: {args.query}", file=sys.stderr)
    results = search_alternatives(args.query)
    print(f"Found {len(results)} relevant discussions", file=sys.stderr)

    competitors = extract_competitor_names(results)
    print(f"Identified {len(competitors)} potential competitors", file=sys.stderr)

    if args.json:
        output = json.dumps({"competitors": competitors, "results": results}, indent=2)
    else:
        output = generate_report(args.query, results, competitors)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Report saved to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
