# Orchestrator Module

This module coordinates the execution of all other modules in sequence.

## API Endpoint

`GET /api/orchestrate`

- Triggers:
  1. Content Research
  2. Course Content Generation
  3. Course Deployment
  4. Content Distribution
- Returns the combined results of all modules.

## Usage

1. Ensure all modules are running on their respective ports:
   - Content Research: 3001
   - Course Generation: 3002
   - Course Deployment: 3003
   - Content Distribution: 3004

2. Run the orchestrator:

```bash
node orchestrator/index.js
```

3. Trigger the full pipeline by visiting:

```
http://localhost:3000/api/orchestrate
```

## Customization

- Modify the orchestrator to add error handling, retries, or parallel execution.
- Add authentication or scheduling as needed.