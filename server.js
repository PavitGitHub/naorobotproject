const express = require('express');
const { upload } = require('./filehandler');
const { nao_controller, yolo_controller, yolo_callback, nao_callback } = require('./Python/pythonHandler.js');

const app = express();
const port = 3000;
var nao = new nao_controller(nao_callback);
var yolo = new yolo_controller(yolo_callback);

app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded or invalid file type.');
  }
  res.status(200).send('File uploaded successfully.');
});

app.post('/test_python_27_input', (req, res) => {
  nao.feedLine("test_input_from_nodejs()");
  res.status(200).send('Success');
});

app.post('/restart-nao-controller', (req, res) => {
  console.warn('RESTARTING NAO CONTROLLER, WARNING: RECONNECTION REQUIRED.');
  nao = new nao_controller(nao_callback);
  res.status(200).send("NAOv5 Evolution Controller successfully restarted, view server console for details.");
});

app.post('/restart-yolo-controller', (req, res) => {
  console.warn('RESTARTING YOLO CONTROLLER.');
  yolo = new yolo_controller(yolo_callback);
  res.status(200).send("YOLOv8 Controller successfully restarted, view server console for details.");
});

app.post('/feed', (req, res) => {
  res.status(200).send("This is a stub route for \'/feed\'.")
})

app.post('/videos', (req, res) => {
  res.status(200).send("This is a stub route for \'/videos\'.")
});

app.get('*', (req, res) => {
  res.status(200).sendFile(__dirname + '\\drumpad.html');
})

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});