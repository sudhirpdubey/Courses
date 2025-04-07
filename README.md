# Courses Modular Web Application

This project is a modular web application designed to automate content research, course generation, deployment, distribution, and analytics. It is built primarily with Node.js and Vue.js (Quasar Framework).

## Modules Overview

### 1. Content Research
- Scrapes trending topics from specified websites.
- Outputs `trending_topics.json`.
- API endpoint: `/api/research` (port 3001)

### 2. Course Content Generation
- Reads trending topics JSON.
- Calls Quasar Alpha API via OpenRouter.
- Outputs `course_content.json`.
- API endpoint: `/api/generate` (port 3002)

### 3. Course Deployment
- Posts course content JSON to a CMS via REST API.
- API endpoint: `/api/deploy` (port 3003)

### 4. Content Distribution
- Generates templated blog and social media posts.
- API endpoint: `/api/distribute` (port 3004)

### 5. Engagement Analytics
- Quasar (Vue.js) dashboard.
- Displays real-time metrics.

## Orchestrator
- Triggers modules sequentially or individually.
- API endpoint: `/api/orchestrate` (port 3000)

## Setup Instructions

1. **Install dependencies**

Navigate to the project root and run:

```bash
npm install
```

2. **Run all module servers**

Open **separate terminals** and run each command **in the project root**:

```bash
node content_research/index.js
node course_generation/index.js
node course_deployment/index.js
node content_distribution/index.js
node orchestrator/index.js
```

> **All five servers must be running simultaneously.**

3. **Trigger the orchestrator**

Visit:

```
http://localhost:3000/api/orchestrate
```

This will sequentially call all modules and return the combined result.

4. **Run Engagement Analytics Dashboard**

Navigate to `engagement_analytics/quasar_project` and run:

```bash
npm install
quasar dev
```

## Integration

- Use the orchestrator to automate the full pipeline.
- Each module can also be triggered independently via its API.
- Customize API keys, endpoints, and templates in respective modules.

## Requirements

- Node.js 16+
- Quasar CLI (`npm install -g @quasar/cli`)
- Access to Quasar Alpha API via OpenRouter
- CMS API credentials

## Notes

- This is a starter scaffold with sample code.
- Extend each module with your specific logic and API keys.
- Ensure CORS and security best practices when deploying.