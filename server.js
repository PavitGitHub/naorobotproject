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

app.post('/feed', (req, res) => {
  res.status(200).send("This is a stub route for \'/feed\'.")
})

app.get('/videos', (req, res) => {
  res.status(200).send("This is a stub route for \'/videos\'.")
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});