import os
import subprocess

# Get the current script directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Command to run the Python script with relative paths
command = [
    'python', 
    'tooltip.py', 
    '--file', 'small.png', 
    '--corner', '9', 
    '--pad', '-7', '-7'
]

# Change to the script directory
os.chdir(script_dir)

# Run the command
subprocess.run(command)
