const express = require('express');
const { upload } = require('./filehandler');
const {nao_controller, yolo_controller} = require('./Python/pythonHandler.js');

const app = express();
const port = 3000;
const nao = new nao_controller( (output) => {console.log(`Recieved Python Output!`)});
const yolo = new yolo_controller((output) => {console.log(`Recieved Python Output!`)});

app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded or invalid file type.');
  }
  res.status(200).send('File uploaded successfully.');
});

app.get('/test_python_27_input', (req, res) => {
  nao.feedLine("test_input_from_nodejs()");
  res.status(200).send('Success');
});

app.post('/restart-nao-controller', (req, res) => {
  nao = new nao_controller( (output) => {console.log(`Recieved Python Output!`)});
  res.status(200).send("NAOv5 Evolution Controller successfully restarted, view server console for details.");
});

app.post('/restart-yolo-controller', (req, res) => {
  yolo = new yolo_controller( (output) => {console.log(`Recieved Python Output!`)});
  res.status(200).send("YOLOv8 Controller successfully restarted, view server console for details.");
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