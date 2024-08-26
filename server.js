const express = require('express');
const { upload } = require('./filehandler');

const app = express();
const port = 3000;

app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded or invalid file type.');
  }
  res.status(200).send('File uploaded successfully.');
});

app.get('/videos', (req, res) => {
  
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});