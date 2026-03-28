#!/usr/bin/env python3
"""
Reddit Pain Point Scraper
Searches Reddit for posts and comments expressing frustration about a topic.
Used by the research-agent in Phase 1 (Validation).

Usage:
    python reddit_scraper.py "outbound sales" --subreddits sales,startups,SaaS --limit 50
    python reddit_scraper.py "property descriptions" --limit 30
"""

import argparse
import json
import sys
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.parse import quote_plus
from urllib.error import HTTPError


def search_reddit(query: str, subreddits: list[str] = None, limit: int = 50, sort: str = "relevance") -> list[dict]:
    """Search Reddit using the public JSON API (no auth required)."""
    results = []

    if subreddits:
        for sub in subreddits:
            url = f"https://www.reddit.com/r/{sub}/search.json?q={quote_plus(query)}&restrict_sr=on&sort={sort}&limit={limit}"
            results.extend(_fetch_posts(url))
    else:
        url = f"https://www.reddit.com/search.json?q={quote_plus(query)}&sort={sort}&limit={limit}"
        results.extend(_fetch_posts(url))

    return results


def _fetch_posts(url: str) -> list[dict]:
    """Fetch posts from a Reddit JSON URL."""
    headers = {"User-Agent": "AIBusinessBuilder/1.0 (research agent)"}
    req = Request(url, headers=headers)

    try:
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
    except HTTPError as e:
        print(f"Warning: Reddit returned {e.code} for {url}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Warning: Failed to fetch {url}: {e}", file=sys.stderr)
        return []

    posts = []
    for child in data.get("data", {}).get("children", []):
        post = child.get("data", {})
        posts.append({
            "title": post.get("title", ""),
            "selftext": post.get("selftext", "")[:500],
            "subreddit": post.get("subreddit", ""),
            "score": post.get("score", 0),
            "num_comments": post.get("num_comments", 0),
            "url": f"https://reddit.com{post.get('permalink', '')}",
            "created_utc": datetime.fromtimestamp(post.get("created_utc", 0)).isoformat(),
            "author": post.get("author", ""),
        })

    return posts


def extract_pain_signals(posts: list[dict]) -> dict:
    """Extract posts that likely contain pain/frustration signals."""
    pain_keywords = [
        "frustrated", "frustrating", "hate", "terrible", "awful", "broken",
        "waste of time", "waste of money", "doesn't work", "can't stand",
        "impossible", "nightmare", "pain", "struggling", "expensive",
        "overpriced", "complicated", "confusing", "slow", "unreliable",
        "anyone else", "am I the only", "help me", "alternative to",
        "looking for", "tired of", "sick of", "fed up", "annoyed",
    ]

    pain_posts = []
    for post in posts:
        text = f"{post['title']} {post['selftext']}".lower()
        matching_keywords = [kw for kw in pain_keywords if kw in text]
        if matching_keywords:
            post["pain_signals"] = matching_keywords
            post["pain_score"] = len(matching_keywords) * post.get("score", 1)
            pain_posts.append(post)

    pain_posts.sort(key=lambda x: x["pain_score"], reverse=True)
    return {
        "total_posts_searched": len(posts),
        "pain_posts_found": len(pain_posts),
        "top_pain_posts": pain_posts[:20],
    }


def generate_report(query: str, results: dict) -> str:
    """Generate a structured research report."""
    report = f"""# Reddit Research Report: "{query}"

## Summary
- Posts searched: {results['total_posts_searched']}
- Posts with pain signals: {results['pain_posts_found']}
- Hit rate: {results['pain_posts_found'] / max(results['total_posts_searched'], 1) * 100:.0f}%

## Top Pain Posts (sorted by relevance)

"""
    for i, post in enumerate(results["top_pain_posts"][:10], 1):
        report += f"""### {i}. {post['title']}
- **Subreddit:** r/{post['subreddit']}
- **Score:** {post['score']} | **Comments:** {post['num_comments']}
- **Pain signals:** {', '.join(post['pain_signals'])}
- **Quote:** "{post['selftext'][:200]}..."
- **Link:** {post['url']}
- **Date:** {post['created_utc']}

"""

    return report


def main():
    parser = argparse.ArgumentParser(description="Search Reddit for pain points about a topic")
    parser.add_argument("query", help="Search query (e.g., 'outbound sales frustration')")
    parser.add_argument("--subreddits", help="Comma-separated subreddits to search", default=None)
    parser.add_argument("--limit", type=int, default=50, help="Max posts to fetch (default: 50)")
    parser.add_argument("--output", help="Output file path (default: stdout)", default=None)
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of report")

    args = parser.parse_args()
    subreddits = args.subreddits.split(",") if args.subreddits else None

    print(f"Searching Reddit for: {args.query}", file=sys.stderr)
    posts = search_reddit(args.query, subreddits=subreddits, limit=args.limit)
    print(f"Found {len(posts)} posts", file=sys.stderr)

    results = extract_pain_signals(posts)

    if args.json:
        output = json.dumps(results, indent=2)
    else:
        output = generate_report(args.query, results)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Report saved to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
