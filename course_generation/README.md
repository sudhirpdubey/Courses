# Course Content Generation Module

This module generates structured course content using trending topics and the Quasar Alpha API.

## API Endpoint

`GET /api/generate`

- Reads `trending_topics.json`.
- Calls Quasar Alpha API via OpenRouter.
- Saves results to `course_content.json`.
- Returns the generated content as JSON.

## Usage

1. Ensure `content_research/trending_topics.json` exists and contains topics.
2. Replace `YOUR_OPENROUTER_API_KEY` in `index.js` with your API key.
3. Run the module:

```bash
node course_generation/index.js
```

4. Trigger content generation by visiting:

```
http://localhost:3002/api/generate
```

5. Check the output in:

```
course_generation/course_content.json
```

## Customization

- Modify the API call and prompt as needed.
- Add error handling or retries for API failures.