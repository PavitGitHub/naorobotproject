const { spawn } = require('child_process');
const path = require('path');

const PYTHON_SCRIPT_PATH_27 = __dirname + '\\2.7\\nao-controller.py';
const PYTHON_SCRIPT_PATH_312 = __dirname + '\\3.12\\cv-controller.py';
const PYTHON_27_ENV_PATH_NAME = 'Python27';
const PYTHON_312_ENV_PATH_NAME = 'Python312';

class nao_controller {

    constructor(stdout_callback, nao_settings)
    {
        this.controller = spawn(PYTHON_27_ENV_PATH_NAME, ['-u', PYTHON_SCRIPT_PATH_27]);

        this.controller.stdout.on('data', (data) => {
            stdout_callback(data);
            const output = data.toString();
        });

        this.controller.stderr.on('data', (data) => {
            console.log(`ERROR: nao_controller stderr encountered:\n${data}`);
        });

        this.controller.on('exit', (code) => {
            console.log(`Nao Controller exited with code: ${code}`);
        });
    }

    feedLine(input)
    {
        try
        {
            this.controller.stdin.write(input + '\n');
        }
        catch (err)
        {
            console.log(`ERROR: Failed to pass input (${input}) to nao controller:\n${err}`);
        }
    }
}

class yolo_controller {
    constructor(stdout_callback, nao_settings)
    {
        this.controller = spawn(PYTHON_312_ENV_PATH_NAME, ['-u', PYTHON_SCRIPT_PATH_312]);

        this.controller.stdout.on('data', (data) => {
            stdout_callback(data);
            const output = data.toString();
        });

        this.controller.stderr.on('data', (data) => {
            console.log(`ERROR: yolo_controller stderr encountered:\n${data}`);
        });

        this.controller.on('exit', (code) => {
            console.log(`YOLO controller exited with code: ${code}`);
        });
    }

    feedLine(input)
    {
        try
        {
            this.controller.stdin.write(input + '\n');
        }
        catch (err)
        {
            console.log(`ERROR: Failed to pass input (${input}) to YOLO controller:\n${err}`);
        }
    }
}

function yolo_callback(output)
{
    console.log(`YC: ${output}`);
}

function nao_callback(output)
{
    console.log(`NC: ${output}`);
}

module.exports = { nao_controller, yolo_controller, yolo_callback, nao_callback };