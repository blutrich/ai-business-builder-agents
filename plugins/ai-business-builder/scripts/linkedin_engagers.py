#!/usr/bin/env python3
"""
LinkedIn Post Engager Outreach Planner
Generates outreach plans and message templates for engaging with people
who interacted with a LinkedIn post. Used by growth-strategist in Phase 5.

IMPORTANT: This script generates outreach PLANS and TEMPLATES.
It does NOT extract engagers from LinkedIn (that requires LinkedIn API
access or tools like Phantombuster, Evaboot, TexAu, or Bond).

The workflow is:
1. Extract engagers using a prospecting tool (see "Extraction Options" below)
2. Use this script to generate a personalized outreach plan with templates
3. Execute the plan through your outreach tool

Usage:
    python linkedin_engagers.py "https://linkedin.com/posts/..." --output plan.md
    python linkedin_engagers.py --help
"""

import argparse
import json
import sys
import re


def extract_post_id(url: str) -> str:
    """Extract the post/activity ID from a LinkedIn URL."""
    patterns = [
        r"activity-(\d+)",
        r"ugcPost-(\d+)",
        r"urn:li:activity:(\d+)",
        r"posts/[^/]+-(\d+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def generate_outreach_plan(post_url: str, topic: str = None, product_name: str = None) -> str:
    """Generate an outreach plan for LinkedIn post engagers."""

    topic_str = topic or "[your topic]"
    product_str = product_name or "[your product]"

    plan = f"""# LinkedIn Post Engager Outreach Plan

## Source Post
{post_url}

## Why This Works

People who engaged with your LinkedIn post have already shown interest in your topic.
They are 3-5x more likely to respond to outreach than cold prospects. This is the
connection between organic content and personalized outreach — the Growth Trifecta.

## Step 1: Extract Engagers

This script generates the PLAN. To get the actual list of engagers, use one of these:

### Option A: Manual (Free, 10-30 min)
1. Open the post on LinkedIn
2. Click on the reactions count to see who liked it
3. Click on the comments to see who commented
4. For each person, note their name, title, and company
5. Add to a spreadsheet

### Option B: Prospecting Tool (Recommended)
Use a LinkedIn scraping tool (Phantombuster, Evaboot, TexAu, or similar):
1. Paste the post URL
2. Extract all reactors and commenters
3. Export as CSV
4. Import into your outreach tool (Apollo, Instantly, Lemlist, or similar)

### Option C: All-in-One Tool (Fastest)
Tools like Bond can:
1. Take the post URL
2. Auto-extract engagers with contact info (emails, phone numbers)
3. Filter by your ideal customer profile
4. Research each person
5. Generate personalized outreach in one workflow

## Step 2: Qualify the List

Not every engager is a prospect. Filter for:
- Title matches your ICP (ideal customer profile)
- Company size/stage fits
- Industry is relevant
- They made a meaningful comment (not just "Great post!")

## Step 3: Personalized Outreach

### Template 1: Comment Reference (Highest Response Rate)
Subject: Saw your comment on {topic_str}

Hi {{{{first_name}}}},

I noticed you commented on my post about {topic_str}. You mentioned {{{{their_comment_snippet}}}}.

That resonated because it's exactly what we're working on with {product_str}. We help [target audience] [achieve specific outcome] without [biggest pain point].

Would you be open to a quick 10-minute call this week? I'd love to hear more about how you handle [problem] today.

Best,
[Your name]

### Template 2: Reactor Outreach
Subject: Fellow {topic_str} enthusiast

Hi {{{{first_name}}}},

We're both interested in {topic_str} — I saw you engaged with my recent LinkedIn post.

I'm building {product_str} which [one sentence value prop]. Given your role as {{{{title}}}} at {{{{company}}}}, I thought this might be relevant.

Would it make sense to connect for 10 minutes this week?

[Your name]

### Template 3: Value-First (Lower Pressure)
Subject: Quick resource on {topic_str}

Hi {{{{first_name}}}},

Since you're interested in {topic_str}, I thought you might find this useful: [link to resource/guide/template].

We put this together based on [data/research/experience]. No strings attached.

If it's helpful and you'd like to chat about how we can help {{{{company}}}} with [specific problem], I'm around this week.

[Your name]

## Step 4: Retargeting with Paid Ads

After extracting engagers, amplify with paid ads:
1. Upload the engager list as a custom audience on Meta Ads
2. Create lookalike audiences from the list
3. Run retargeting ads on YouTube, Facebook, Instagram
4. Budget: Start with $500-1000/month on retargeting only
5. These people already showed interest, so conversion rates are much higher

## Metrics to Track
- Response rate from engagers vs. cold outreach (expect 2-5x improvement)
- Meeting booking rate
- Conversion rate to paid customer
- Cost per acquisition through this channel
"""
    return plan


def main():
    parser = argparse.ArgumentParser(
        description="Generate outreach plans for LinkedIn post engagers. "
                    "NOTE: This generates plans and templates, not extraction. "
                    "Use a prospecting tool (Phantombuster, Bond, etc.) to extract engagers first."
    )
    parser.add_argument("post_url", nargs="?", help="LinkedIn post URL")
    parser.add_argument("--output", help="Output file path (default: stdout)", default=None)
    parser.add_argument("--topic", help="Topic of the post (used in templates)", default=None)
    parser.add_argument("--product", help="Your product name (used in templates)", default=None)

    args = parser.parse_args()

    if not args.post_url:
        parser.print_help()
        sys.exit(1)

    post_id = extract_post_id(args.post_url)
    if post_id:
        print(f"Post ID extracted: {post_id}", file=sys.stderr)
    else:
        print("Warning: Could not extract post ID from URL", file=sys.stderr)

    plan = generate_outreach_plan(args.post_url, topic=args.topic, product_name=args.product)

    if args.output:
        with open(args.output, "w") as f:
            f.write(plan)
        print(f"Plan saved to {args.output}", file=sys.stderr)
    else:
        print(plan)


if __name__ == "__main__":
    main()
