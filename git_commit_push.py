import os
import shlex
import subprocess
import logging

def run_command(command):
    """Executes a system command and returns the output, error and exit code."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    output, error = process.communicate()
    exit_code = process.returncode
    return output, error, exit_code

def commit_and_push_changes():
    """Commits and pushes changes to the remote repository."""
    user_input = input("Enter your commit message: ")  
    safe_user_input = shlex.quote(user_input)
    # Determine the current branch name dynamically
    current_branch_command = "git rev-parse --abbrev-ref HEAD"
    current_branch_output, current_branch_error, current_branch_exit_code = run_command(current_branch_command)
    if current_branch_exit_code != 0:
        logging.error(f"Error determining current branch: {current_branch_error}")
        return
    current_branch = current_branch_output.strip()
    logging.info(f"Current branch is {current_branch}")
    
    commands = [
        "git add .",
        f"git commit -m \"{safe_user_input}\"",
        f"git push origin {current_branch}"
    ]
    for command in commands:
        output, error, exit_code = run_command(command)
        if exit_code == 0:
            logging.info(f"Successfully executed: {command}")
        else:
            logging.error(f"Error running command '{command}': {error}")
            break

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    commit_and_push_changes()