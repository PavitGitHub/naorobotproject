const express = require('express');
const { upload } = require('./uploads/filehandler');
const { computerVision, translateAudio, restartNaoController, restartCVController } = require('./controllers/dataController');
const { setUser, verifyUser } = require('./controllers/userController');
const { getIPAddress } = require('./utils/ip');
const DEBUG = true;


const app = express();
const port = 3000;
app.set('view engine', 'ejs');

app.post('/setUser', setUser);

app.post('/verifyUser', verifyUser);

app.post('/computer-vision', computerVision);

app.post('/translate', translateAudio);

app.post('/restart-nao-controller', restartNaoController);

app.post('/restart-cv-controller', restartCVController);

app.get('*', (req, res) => 
{
  let ipAddress = DEBUG ? 'localhost' : getIPAddress();
  res.render(process.cwd() + './ejs/drumpad.ejs', { ipAddress, port });
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});