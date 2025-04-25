const express = require('express');

const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Basic route
app.get('/', (req, res) => {
  res.send("<h1>hi cv!</h1>");
});

// Route to handle GET requests to /api
app.get('/api', (req, res) => {
  res.json({ message: 'Hello from the API!' });
});

// Route to handle POST requests to /contact


// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});