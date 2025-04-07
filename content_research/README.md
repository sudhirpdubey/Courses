# Content Research Module

This module scrapes trending topics from specified websites and outputs a JSON file.

## API Endpoint

`GET /api/research`

- Scrapes trending topics.
- Saves results to `trending_topics.json`.
- Returns the topics as JSON.

## Usage

1. Run the module:

```bash
node content_research/index.js
```

2. Trigger scraping by visiting:

```
http://localhost:3001/api/research
```

3. Check the output in:

```
content_research/trending_topics.json
```

## Customization

- Update the URL and scraping logic in `index.js` to target your preferred websites.
- Adjust the CSS selectors as needed.