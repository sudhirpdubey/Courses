# Course Deployment Module

This module posts generated course content to a CMS via REST API.

## API Endpoint

`GET /api/deploy`

- Reads `course_content.json`.
- Posts data to the CMS API.
- Returns the CMS response as JSON.

## Usage

1. Ensure `course_generation/course_content.json` exists and contains course data.
2. Replace `YOUR_CMS_API_KEY` in `index.js` with your CMS API key.
3. Update the CMS API URL if needed.
4. Run the module:

```bash
node course_deployment/index.js
```

5. Trigger deployment by visiting:

```
http://localhost:3003/api/deploy
```

## Customization

- Modify the CMS API URL and headers as needed.
- Add error handling or retries for API failures.