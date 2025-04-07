# Content Distribution Module

This module generates templated blog and social media posts based on course content.

## API Endpoint

`GET /api/distribute`

- Reads `course_content.json`.
- Generates blog and social media post templates.
- Saves output to text files.
- Returns generated content as JSON.

## Usage

1. Ensure `course_generation/course_content.json` exists and contains course data.
2. Run the module:

```bash
node content_distribution/index.js
```

3. Trigger content distribution by visiting:

```
http://localhost:3004/api/distribute
```

4. Check the generated files:

```
content_distribution/blog_post.txt
content_distribution/social_post.txt
```

## Customization

- Modify the templates in `index.js` as needed.
- Extend to generate content for multiple courses or platforms.