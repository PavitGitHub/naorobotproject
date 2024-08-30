const express = require('express');
const { upload } = require('./filehandler');
const {startNao_controller, nao_controller} = require('./Python/pythonHandler.js');

const app = express();
const port = 3000;
const nao = new nao_controller( (output) => {console.log(`Recieved Python Output!`)});;

app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded or invalid file type.');
  }
  res.status(200).send('File uploaded successfully.');
});

app.get('/test_python_initalise', (req, res) => {
  nao.feedLine("test_input_from_nodejs()");
  res.status(200).send('Success');
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