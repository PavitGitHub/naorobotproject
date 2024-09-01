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
            console.log(`nao_controller stdout: ${output}`);
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
            console.log(`Passed ${input} to nao controller.\n`);
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
            console.log(`YOLO_controller stdout: ${output}`);
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
            console.log(`Passed ${input} to YOLO controller.\n`);
        }
        catch (err)
        {
            console.log(`ERROR: Failed to pass input (${input}) to YOLO controller:\n${err}`);
        }
    }
}

module.exports = { nao_controller, yolo_controller };