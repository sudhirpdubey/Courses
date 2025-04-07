const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

// Endpoint to orchestrate all modules
app.get('/api/orchestrate', async (req, res) => {
  try {
    // 1. Trigger Content Research
    const research = await axios.get('http://localhost:3001/api/research');
    console.log('Research done');

    // 2. Trigger Course Generation
    const generation = await axios.get('http://localhost:3002/api/generate');
    console.log('Generation done');

    // 3. Trigger Course Deployment
    const deployment = await axios.get('http://localhost:3003/api/deploy');
    console.log('Deployment done');

    // 4. Trigger Content Distribution
    const distribution = await axios.get('http://localhost:3004/api/distribute');
    console.log('Distribution done');

    res.json({
      success: true,
      research: research.data,
      generation: generation.data,
      deployment: deployment.data,
      distribution: distribution.data
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ success: false, error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Orchestrator running on port ${PORT}`);
});