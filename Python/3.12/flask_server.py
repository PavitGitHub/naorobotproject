import subprocess
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/nao/command', methods=['POST'])
def control_nao():
    try:
        data = request.json
        command = data.get('command')
        print(f"Received command: {command}")

        # Asynchronously execute the command, allowing multiple requests to be handled simultaneously
        process = subprocess.Popen(['python27', 'C:/nao-robot/naorobotproject/Python/2.7/imu_control_test.py', command],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Set a timeout of 20 seconds for command execution
        try:
            output, error = process.communicate(timeout=20)
        except subprocess.TimeoutExpired:
            process.kill()  # Terminate the process if it exceeds the timeout
            output, error = process.communicate()
            print(f"Command {command} timed out")
            return jsonify({"status": "error", "message": "Command timed out"}), 500

        if process.returncode == 0:
            print(f"Command {command} executed successfully")
            return jsonify({"status": f"Command {command} executed successfully"}), 200
        else:
            print(f"Error executing command: {error.decode('utf-8')}")
            return jsonify({"status": "error", "message": error.decode('utf-8')}), 500

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Enable multithreading to handle multiple requests
    app.run(host='0.0.0.0', port=5000, threaded=True)
