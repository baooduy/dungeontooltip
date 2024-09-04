import os
import subprocess

# Get the current script directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Command to run the Python script with relative paths
command = [
    'python', 
    'tooltip.py', 
    '--file', 'big.png', 
    '--corner', '12', 
    '--pad', '-10', '-10'
]

# Change to the script directory
os.chdir(script_dir)

# Run the command
subprocess.run(command)
