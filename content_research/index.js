const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const app = express();
const PORT = 3001;

// Endpoint to trigger scraping
app.get('/api/research', async (req, res) => {
  try {
    // Placeholder: scrape trending topics from a website
    const response = await axios.get('https://example.com/trending');
    const $ = cheerio.load(response.data);

    const topics = [];
    $('.trending-topic').each((i, elem) => {
      topics.push($(elem).text().trim());
    });

    // Save to JSON file
    fs.writeFileSync('content_research/trending_topics.json', JSON.stringify({ topics }, null, 2));

    res.json({ success: true, topics });
  } catch (error) {
    console.error(error);
    res.status(500).json({ success: false, error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Content Research module running on port ${PORT}`);
});