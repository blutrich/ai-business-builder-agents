# ClimbClaw - WhatsApp Integration Tech Stack Advice

Great that you've done 3 weeks of research on the climbing coach market! Before diving into the tech stack for WhatsApp integration, here's what I'd recommend:

## Recommended Tech Stack for WhatsApp Integration

### WhatsApp Business API Access
You have two main paths:

1. **WhatsApp Cloud API (Meta)** - The official, free-tier option hosted by Meta. This is the best starting point for a new project. You get 1,000 free service conversations per month and can scale from there.

2. **WhatsApp Business Solution Provider (BSP)** - Services like Twilio, MessageBird, or Vonage that wrap the WhatsApp API with additional features. Easier to set up but adds cost.

**My recommendation:** Start with the **WhatsApp Cloud API** directly. It's free to start, well-documented, and gives you full control.

### Backend Stack (with Claude Agent SDK)

Since you want to use the Claude Agent SDK, here's the stack I'd suggest:

- **Runtime:** Node.js (TypeScript) or Python
- **Claude Agent SDK:** `@anthropic-ai/sdk` (Node) or `anthropic` (Python) - for the AI coaching logic
- **WhatsApp Cloud API:** Direct HTTP integration via webhooks
- **Database:** PostgreSQL (for user profiles, conversation history, training plans) or MongoDB if you prefer flexible schemas
- **Hosting:** Railway, Render, or a simple VPS - you need a persistent server for webhooks

### Architecture Overview

```
WhatsApp Cloud API --> Webhook Endpoint (your server)
                          |
                          v
                    Message Router
                          |
                          v
                   Claude Agent SDK
                   (coaching logic)
                          |
                          v
                    Database (user state,
                    training history)
                          |
                          v
                    Response --> WhatsApp Cloud API
```

### Key Technical Components

1. **Webhook Server** - Receives incoming messages from WhatsApp. Express.js (Node) or FastAPI (Python) works well.

2. **Message Handler** - Parses incoming messages (text, images of climbing routes, voice notes) and routes them to the right Claude agent flow.

3. **Claude Agent SDK Integration** - Build your coaching agent with system prompts tuned for climbing coaching. Use conversation history from your DB to maintain context across sessions.

4. **Session Management** - WhatsApp conversations are stateless from Meta's perspective. You need to maintain user state (current training plan, grade level, injury history, etc.) in your database.

5. **Template Messages** - WhatsApp requires pre-approved templates for outbound/proactive messages (e.g., "Time for your training session!"). Plan these early.

### Specific Package Recommendations (Node.js/TypeScript)

```
- @anthropic-ai/sdk          # Claude Agent SDK
- express or fastify          # Webhook server
- axios or node-fetch         # WhatsApp API calls
- prisma or drizzle           # Database ORM
- zod                         # Input validation
- bull or bullmq              # Job queue (for async processing)
```

### Specific Package Recommendations (Python)

```
- anthropic                   # Claude Agent SDK
- fastapi + uvicorn           # Webhook server
- httpx                       # WhatsApp API calls
- sqlalchemy or prisma-client # Database ORM
- pydantic                    # Input validation
- celery or arq               # Job queue
```

## Important Considerations

### Before You Code This Weekend

1. **Apply for WhatsApp Cloud API access** NOW - Go to developers.facebook.com, create a Meta Business account, and set up a WhatsApp Business app. You'll get a test phone number immediately, but production access takes a few days for verification.

2. **WhatsApp has strict policies** - You can't send unsolicited marketing messages. Conversations must be user-initiated (or use approved templates). Make sure your coaching model fits within their business messaging policies.

3. **Rate limits** - The Cloud API has rate limits. For a coaching app, this likely won't be an issue early on, but design with queuing in mind.

4. **Media handling** - If climbers will send photos/videos of routes or their climbing, you'll need to handle media downloads from WhatsApp's CDN (URLs expire after a few days).

### Weekend MVP Suggestion

For a weekend build, I'd scope it to:
- Webhook server that receives WhatsApp messages
- Claude Agent SDK integration with a climbing coach system prompt
- Simple conversation history stored in SQLite (upgrade to Postgres later)
- Text-only responses (skip media for now)

This gets you a working prototype you can test with real climbing coaches or climbers by Sunday night.

## One More Thing

You mentioned 3 weeks of research. Before spending the weekend coding, make sure you've validated that climbing coaches actually want to interact with their clients through WhatsApp (vs. a dedicated app, email, etc.). Talk to 5 coaches. If they're already using WhatsApp informally with clients, that's a strong signal. If they're not, the tech stack doesn't matter yet.
