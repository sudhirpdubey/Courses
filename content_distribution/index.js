const express = require('express');
const fs = require('fs');
const app = express();
const PORT = 3004;

// Endpoint to generate distribution content
app.get('/api/distribute', async (req, res) => {
  try {
    // Read course content
    const courseData = JSON.parse(fs.readFileSync('course_generation/course_content.json'));

    // Placeholder: Generate blog and social media posts
    const blogPost = `New Course: ${courseData.courses?.[0]?.title || 'Untitled'}\n\n${courseData.courses?.[0]?.description || 'No description.'}`;
    const socialPost = `Check out our new course: ${courseData.courses?.[0]?.title || 'Untitled'}! #OnlineLearning`;

    // Save to files
    fs.writeFileSync('content_distribution/blog_post.txt', blogPost);
    fs.writeFileSync('content_distribution/social_post.txt', socialPost);

    res.json({ success: true, blogPost, socialPost });
  } catch (error) {
    console.error(error);
    res.status(500).json({ success: false, error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Content Distribution module running on port ${PORT}`);
});