const { nao_controller, yolo_controller, yolo_callback, nao_callback } = require('../Python/pythonHandler.js');
var nao = new nao_controller(nao_callback);
var yolo = new yolo_controller(yolo_callback);

const computerVision = function(req, res)
{
    nao.feedLine('print("{}".format(str(get_camera_image())))')
    while (!nao.new_output);
    let image_str = nao.getLastOutput();
    res.status(200).send(`Success: Image Retrieved:\n${image_str}`);
}

const translateAudio = function(req, res)
{

}

const listen = function(req, res)
{
    try
    {
        nao.feedLine("listen(10000)");
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
    console.warn('RESTARTING YOLO CONTROLLER.');
    yolo = new yolo_controller(yolo_callback);
    res.status(200).send({message: "YOLOv8 Controller successfully restarted, view server console for details."});
}

module.exports = { computerVision, translateAudio, listen, restartNaoController, restartCVController, nao };