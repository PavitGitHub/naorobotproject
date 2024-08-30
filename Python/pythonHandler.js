const { spawn } = require('child_process');
const path = require('path');

const PYTHON_SCRIPT_PATH_27 = __dirname + '\\2.7\\nao-controller.py';
const PYTHON_SCRIPT_PATH_312 = __dirname + '\\3.12\\state-machine.py';

class nao_controller {

    constructor(stdout_callback, nao_settings)
    {
        this.controller = spawn('Python27', ['-u', PYTHON_SCRIPT_PATH_27]);

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

module.exports = { nao_controller };