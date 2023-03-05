import subprocess

def run_command(command):
    # Run the command in the terminal and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

    # If the command was successful, return the output
    if result.returncode == 0:
        return result.stdout.strip()

    # If the command failed, print the error message and return None
    else:
        return result.stderr.strip()


command = 'slither smartcontract.sol'
output = run_command(command)

# Print the analysis results to the console
