# ClimbClaw -- Product Requirements Document (PRD)

## Building on Base44

Great news -- you already have validated demand from competitive climbers via your landing page. That is the hardest part done. Now we need to turn that interest into a product people will pay for. Below is a full PRD you can use to build ClimbClaw on Base44.

---

## 1. Product Overview

**Product Name:** ClimbClaw

**One-Liner:** The all-in-one training platform for competitive climbers -- personalized plans, session tracking, nutrition, technique analysis, and coach tools.

**Target Users:**
- **Primary:** Competitive climbers (bouldering, sport, lead) training 3-7 days/week
- **Secondary:** Climbing coaches managing multiple athletes
- **Tertiary:** Serious recreational climbers looking to break through plateaus

**Platform:** Web app built on Base44 (mobile-responsive, PWA-capable)

**Core Value Proposition:** Competitive climbers currently piece together training across spreadsheets, generic fitness apps, and coach texts. ClimbClaw consolidates everything into one platform purpose-built for climbing performance.

---

## 2. MVP Scope -- Ship in One Week

**CRITICAL DECISION:** Do NOT build all five features at once. Pick ONE core feature for the MVP, ship it in a week, and layer on the rest based on user feedback.

**Recommended MVP Feature: Session Tracking + Personalized Training Plans**

These two are tightly coupled and deliver the most immediate value. A climber can log sessions and follow a structured plan from day one.

**Features to defer to v2/v3:**
- Nutrition guidance (v2)
- Technique video analysis (v3 -- requires significant AI/ML integration)
- Coach dashboard (v2 -- once you have enough individual users)

---

## 3. Data Model (Base44 Entities)

### Entity: User
| Field | Type | Description |
|-------|------|-------------|
| name | string | Full name |
| email | string | Login email |
| role | enum | "athlete" or "coach" |
| climbing_discipline | enum | "bouldering", "sport", "lead", "multi" |
| current_grade | string | Current max grade (e.g. "V8", "7b+") |
| goal_grade | string | Target grade |
| training_days_per_week | number | Available training days (1-7) |
| experience_years | number | Years of climbing experience |
| injuries | text | Current injuries/limitations |
| coach_id | relation | Link to coach User (optional) |
| created_at | datetime | Account creation date |

### Entity: TrainingPlan
| Field | Type | Description |
|-------|------|-------------|
| user_id | relation | Owner of the plan |
| name | string | Plan name (e.g. "V10 Bouldering Block") |
| goal | text | What this plan targets |
| start_date | date | Plan start |
| end_date | date | Plan end |
| phase | enum | "base", "strength", "power", "performance", "deload" |
| status | enum | "active", "completed", "paused" |
| weeks | number | Duration in weeks |
| notes | text | Coach or AI notes |

### Entity: TrainingSession (the daily workout)
| Field | Type | Description |
|-------|------|-------------|
| plan_id | relation | Parent training plan |
| user_id | relation | Athlete |
| date | date | Scheduled date |
| session_type | enum | "climbing", "hangboard", "campus", "antagonist", "cardio", "rest" |
| focus | enum | "endurance", "strength", "power", "technique", "projecting" |
| prescribed_exercises | json | Array of exercises with sets/reps/rest |
| status | enum | "upcoming", "completed", "skipped" |
| duration_minutes | number | Planned duration |

### Entity: SessionLog (what actually happened)
| Field | Type | Description |
|-------|------|-------------|
| session_id | relation | Linked planned session (optional) |
| user_id | relation | Athlete |
| date | datetime | When the session happened |
| location | string | Gym or crag name |
| session_type | enum | Same as TrainingSession |
| duration_minutes | number | Actual duration |
| perceived_effort | number | RPE 1-10 |
| energy_level | enum | "low", "moderate", "high" |
| climbs_logged | json | Array of {grade, style, attempts, sent, notes} |
| exercises_logged | json | Array of {name, sets, reps, weight, rest, notes} |
| skin_condition | enum | "fresh", "good", "tender", "split" |
| notes | text | Free text notes |
| mood | enum | "great", "good", "neutral", "tired", "frustrated" |

### Entity: Exercise (library)
| Field | Type | Description |
|-------|------|-------------|
| name | string | Exercise name |
| category | enum | "hangboard", "campus", "antagonist", "core", "mobility", "climbing_drill" |
| description | text | How to perform |
| muscle_groups | json | Target muscles |
| difficulty | enum | "beginner", "intermediate", "advanced" |
| video_url | string | Demo video link (optional) |

### Entity: NutritionLog (v2)
| Field | Type | Description |
|-------|------|-------------|
| user_id | relation | Athlete |
| date | date | Log date |
| meals | json | Array of {meal_type, description, calories, protein, carbs, fat} |
| water_liters | number | Water intake |
| supplements | json | Array of supplement names |
| notes | text | How they felt |

### Entity: CoachAthleteRelation (v2)
| Field | Type | Description |
|-------|------|-------------|
| coach_id | relation | Coach user |
| athlete_id | relation | Athlete user |
| status | enum | "pending", "active", "ended" |
| start_date | date | Coaching start |
| notes | text | Coach notes on athlete |

---

## 4. MVP Feature Specs

### 4.1 Personalized Training Plan Generator

**User Flow:**
1. Athlete completes onboarding questionnaire (grade, goals, available days, experience, injuries)
2. System generates a 4-week training plan using AI (Base44 AI agent)
3. Plan displays as a weekly calendar with daily sessions
4. Athlete can adjust/swap sessions
5. Plan auto-advances and generates next block based on logged performance

**AI Agent Prompt (for Base44 AI Agent):**
```
You are a climbing coach AI. Generate a 4-week training plan based on:
- Current grade: {current_grade}
- Goal grade: {goal_grade}
- Discipline: {climbing_discipline}
- Available days: {training_days_per_week}
- Experience: {experience_years} years
- Injuries: {injuries}

Follow periodization principles:
- Week 1-2: Volume/base building
- Week 3: Intensity peak
- Week 4: Deload

Each session should include: session_type, focus, duration, and specific exercises with sets/reps/rest.
Output as JSON matching the TrainingSession schema.
```

**Key Rules:**
- Never schedule climbing on consecutive days for beginners
- Include antagonist training at least 2x/week
- Deload week reduces volume by 40-50%
- Hangboard sessions require 48h recovery

### 4.2 Session Tracking

**User Flow:**
1. Athlete opens today's planned session (or starts a free session)
2. Timer starts automatically
3. For climbing: log each climb (grade, attempts, send/no-send, style)
4. For training: log exercises with actual sets/reps/weight
5. Rate perceived effort (RPE 1-10), energy, skin condition, mood
6. Save session -- data feeds into progress analytics

**Quick-Log UI Requirements:**
- Large touch-friendly buttons for grade selection
- Swipe to mark "sent" vs "attempted"
- Auto-suggest grades based on recent history
- Timer with rest period alerts
- Minimal typing -- mostly taps and swipes

### 4.3 Progress Dashboard

**Metrics to Display:**
- Grade pyramid (distribution of sends by grade)
- Volume over time (sessions/week, climbs/session)
- RPE trend (are they adapting or overtraining?)
- Send rate by grade (attempts vs sends)
- Training plan adherence %
- Personal records timeline

**Charts:**
- Line chart: weekly volume trend
- Bar chart: grade pyramid
- Heatmap: training consistency calendar
- Gauge: current week adherence

---

## 5. Pages / Navigation Structure

### Athlete Pages:
1. **Dashboard** -- Today's session, quick stats, streak counter
2. **Training Plan** -- Calendar view of current plan, upcoming sessions
3. **Log Session** -- Quick-log interface for climbing and training
4. **Progress** -- Charts, PRs, grade pyramid
5. **Exercise Library** -- Browse exercises with filters
6. **Profile/Settings** -- Goals, preferences, coach link

### Coach Pages (v2):
1. **Coach Dashboard** -- Overview of all athletes
2. **Athlete Detail** -- Individual athlete progress, plan management
3. **Plan Builder** -- Drag-and-drop plan creation
4. **Messages** -- Communication with athletes

---

## 6. Base44 Build Prompt

Use this prompt to create the initial app in Base44:

```
Build a climbing training app called "ClimbClaw" with the following:

ENTITIES:
1. User - with fields: name (string), email (string), role (enum: athlete/coach), climbing_discipline (enum: bouldering/sport/lead/multi), current_grade (string), goal_grade (string), training_days_per_week (number), experience_years (number), injuries (text)

2. TrainingPlan - with fields: user_id (relation to User), name (string), goal (text), start_date (date), end_date (date), phase (enum: base/strength/power/performance/deload), status (enum: active/completed/paused), weeks (number)

3. TrainingSession - with fields: plan_id (relation to TrainingPlan), user_id (relation to User), date (date), session_type (enum: climbing/hangboard/campus/antagonist/cardio/rest), focus (enum: endurance/strength/power/technique/projecting), prescribed_exercises (json), status (enum: upcoming/completed/skipped), duration_minutes (number)

4. SessionLog - with fields: session_id (relation to TrainingSession), user_id (relation to User), date (datetime), location (string), session_type (enum), duration_minutes (number), perceived_effort (number 1-10), energy_level (enum: low/moderate/high), climbs_logged (json), exercises_logged (json), skin_condition (enum: fresh/good/tender/split), notes (text), mood (enum: great/good/neutral/tired/frustrated)

5. Exercise - with fields: name (string), category (enum: hangboard/campus/antagonist/core/mobility/climbing_drill), description (text), muscle_groups (json), difficulty (enum: beginner/intermediate/advanced), video_url (string)

PAGES:
1. Dashboard - shows today's planned session, weekly summary stats, training streak, next session preview
2. Training Plan - calendar view showing current active plan with daily sessions, ability to view session details
3. Log Session - quick-log interface with: climb logger (grade picker, attempts, send toggle), exercise logger (sets/reps/weight), RPE slider, energy and mood selectors, timer
4. Progress - grade pyramid chart, volume trend line chart, RPE trend, send rate stats, training adherence percentage
5. Exercise Library - searchable/filterable grid of exercises with descriptions
6. Profile - user settings, goals, current grade, edit preferences

DESIGN:
- Dark theme with accent color #FF6B35 (climbing orange)
- Clean, modern, mobile-first design
- Large touch targets for gym use
- Minimal text input, maximum tap/swipe interactions

AI AGENT:
Create an AI agent called "TrainingPlanGenerator" that takes user profile data and generates a personalized 4-week training plan following climbing periodization principles. It should output TrainingSession records with specific exercises.
```

---

## 7. Success Metrics

| Metric | Target (Month 1) | Target (Month 3) |
|--------|-------------------|-------------------|
| Registered users | 50 | 250 |
| Weekly active users | 30 | 150 |
| Sessions logged/week | 100 | 750 |
| Plan completion rate | 40% | 60% |
| NPS score | >30 | >50 |

---

## 8. Technical Considerations for Base44

- **JSON fields:** Use JSON type for climbs_logged, exercises_logged, prescribed_exercises -- these are arrays of objects that would be awkward as separate entities
- **AI Agent:** Base44 AI agents can generate training plans. Feed the user profile data and get back structured session data
- **Backend Functions:** Use Base44 backend functions for progress calculations (grade pyramid, volume trends, adherence %)
- **Auth:** Base44 handles auth out of the box -- just configure the User entity as the auth entity
- **Responsive Design:** Base44 generates responsive layouts -- test on phone since climbers will log at the gym

---

## 9. Phased Rollout

### Week 1 (MVP):
- Onboarding flow
- AI training plan generation
- Session logging (climbing + exercises)
- Basic dashboard with today's session

### Week 2-3 (v1.1):
- Progress charts and grade pyramid
- Exercise library with demos
- Plan adjustment and regeneration
- Push notification reminders

### Month 2 (v2):
- Coach dashboard and athlete management
- Nutrition logging
- Social features (share sends, challenge friends)
- Integration with climbing gym APIs (if available)

### Month 3+ (v3):
- Video upload and technique analysis (AI-powered)
- Competition prep modules
- Wearable integration (heart rate, recovery)
- Marketplace for coach-created plans

---

## 10. Immediate Next Steps

1. **Copy the Base44 Build Prompt** (Section 6) and create the app
2. **Seed the Exercise Library** with 30-40 common climbing exercises
3. **Test the AI plan generator** with 3-4 different climber profiles
4. **Share the preview URL** with 5-10 of your most engaged landing page leads
5. **Collect feedback** and iterate before wider launch

You have demand. You have a platform. Ship the MVP this week and let real climbers tell you what to build next.
