from flask import Flask, render_template, request, jsonify
import subprocess
import getpass
import traceback
import os
import sys

# Path to the lock file
LOCK_FILE = '/tmp/veracrypt_mount.lock'

# Check if the lock file exists
if os.path.exists(LOCK_FILE):
    print("Script is already running. Aborting.")
    sys.exit(0)

# Create the lock file
with open(LOCK_FILE, 'w') as f:
    f.write(str(os.getpid()))

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/mount', methods=['POST'])
def mount_volume():
    # Retrieve password, hidden password, and selected device from the form
    password = request.form.get('password')
    hidden_password = request.form.get('hidden-password')
    selected_device = request.form.get('device')

    # Define mount points and devices based on the selected option
    if selected_device == 'onion':
        device = '/dev/sda5'
        user=getpass.getuser()
        mount_point = f'/media/{user}/onion'
    elif selected_device == 'backups':
        device = '/dev/sdb1'
        user=getpass.getuser()
        mount_point = f'/media/{user}/backups'
    else:
        return jsonify({'status': 'error', 'message': 'Invalid device selected'})

    # Execute VeraCrypt command to mount the volume
    try:
        # Construct VeraCrypt command
        command = f'sudo veracrypt -t --non-interactive --password={password}'
        if hidden_password:  # If a hidden password is provided, append it to the command
            command += f' --pim=0 --protect-hidden=yes --protection-password={hidden_password}'
        command += f' {device} {mount_point}'

        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return jsonify({'status': 'success', 'message': 'Volume mounted successfully'})
    except subprocess.CalledProcessError as e:
        # Get the full error message including the traceback
        traceback_message = traceback.format_exc()
        # Write the error message to the log file
        user = getpass.getuser()
        log_path = f'/home/{user}/tools/scripts/mount/mount_fail.log'
        with open(log_path, 'w') as f:
            f.write(traceback_message)
        return jsonify({'status': 'error', 'message': f'Failed to mount volume. Check logs for more information.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5045)  # Run the Flask app on port 5045

# Remove the lock file
os.remove(LOCK_FILE)
