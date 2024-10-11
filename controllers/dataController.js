const { nao_controller, cv_controller, cv_callback, nao_callback } = require('../Python/pythonHandler.js');
const os = require('os');
const fs = require('fs');
var nao = new nao_controller(nao_callback);
var cv = new cv_controller(yolo_callback);

const computerVision = function(req, res)
{
    nao.feedLine('get_frame');
    while (!nao.new_output);
    let output = nao.getLastOutput();
    if (output.includes('ERROR'))
    {
        console.error(`NAO ERROR: ${output}`);
        return res.status(500).send(output);
    }
    let filename = nao.getLastOutput().split(':')[1];
    cv.feedLine(`processImages([${os.pwd() + '/tempFileStorage/' + filename}])`);
    while (!cv.new_output);
    try
    {
        let detections = JSON.parse(cv.getLastOutput().split(':')[1]);
    }
    catch (err)
    {
        console.error(err);
        res.status(500).send(err);
    }
    
    console.log(detections);
    console.warn(`Deleting Temporary File: ${os.pwd() + '/tempFileStorage/' + filename} . . .`);
    fs.unlink(`${os.pwd() + '/tempFileStorage/' + filename}`);
    console.warn('File Deleted.');

    JSON.parse(detections);
    let tts = ''
    for (let i = 0; i < detections.length; i++)
    {
        tts += `There is a ${detections[i][0]} in the ${detections[i][1]} of my vision. `;
    }
    nao.feedLine(`tts \"${tts}\"`);
    res.status(200).send(`Success: Image Retrieved:\n${image_str}`);
}

const translateAudio = function(req, res)
{

}

const listen = function(req, res)
{
    try
    {
        nao.feedLine("listen 10");
        while (!nao.new_output);
        if (output.includes('ERROR'))
        {
            console.error(`NAO ERROR: ${output}`);
            return res.status(500).send(output);
        }
        let filename = nao.getLastOutput().split(':')[1];
        


    }
    catch (e)
    {
        return res.status(500).send(e);
    }
    res.status(200).send('Listening')
}

const restartNaoController = function(req, res)
{
    console.warn('RESTARTING NAO CONTROLLER, WARNING: RECONNECTION REQUIRED.');
    nao = new nao_controller(nao_callback);
    res.status(200).send({message: "NAOv5 Evolution Controller successfully restarted, view server console for details."});
}

const restartCVController = function(req, res)
{
    console.warn('RESTARTING CV CONTROLLER.');
    cv = new cv_controller(cv_callback);
    res.status(200).send({message: "CV Controller successfully restarted, view server console for details."});
}

module.exports = { computerVision, translateAudio, listen, restartNaoController, restartCVController, nao };