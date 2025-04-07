const express = require('express');
const axios = require('axios');
const fs = require('fs');
const app = express();
const PORT = 3003;

// Endpoint to deploy course content
app.get('/api/deploy', async (req, res) => {
  try {
    // Read course content
    const courseData = JSON.parse(fs.readFileSync('course_generation/course_content.json'));

    // Placeholder: Post to CMS API
    const response = await axios.post('https://courses.sudhirdubey.com/api/courses', courseData, {
      headers: {
        'Authorization': 'Bearer YOUR_CMS_API_KEY',
        'Content-Type': 'application/json'
      }
    });

    res.json({ success: true, cmsResponse: response.data });
  } catch (error) {
    console.error(error);
    res.status(500).json({ success: false, error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Course Deployment module running on port ${PORT}`);
});