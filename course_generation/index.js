const express = require('express');
const axios = require('axios');
const fs = require('fs');
const app = express();
const PORT = 3002;

// Endpoint to generate course content
app.get('/api/generate', async (req, res) => {
  try {
    // Read trending topics
    const topicsData = JSON.parse(fs.readFileSync('content_research/trending_topics.json'));

    // Placeholder: Call Quasar Alpha API via OpenRouter
    const response = await axios.post('https://openrouter.ai/api/quasar-alpha', {
      prompt: `Generate course content for topics: ${topicsData.topics.join(', ')}`
    }, {
      headers: {
        'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY'
      }
    });

    const courseContent = response.data;

    // Save to JSON file
    fs.writeFileSync('course_generation/course_content.json', JSON.stringify(courseContent, null, 2));

    res.json({ success: true, courseContent });
  } catch (error) {
    console.error(error);
    res.status(500).json({ success: false, error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Course Generation module running on port ${PORT}`);
});