import os
import shlex
import subprocess
import logging

def run_command(command):
    """Executes a system command and returns the output, error and exit code."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    output, error = process.communicate()
    exit_code = process.returncode
    if exit_code == 0:
        logging.info(f"Successfully executed: {command}")
    else:
        if error:
            logging.error(f"Error running command '{command}': {error}")
        else:
            logging.error(f"Command '{command}' executed with exit code {exit_code} but no error message was provided.")
        logging.error("Full error:", exc_info=True)
    return output, error, exit_code

def commit_and_push_changes():
    """Commits and pushes changes to the remote repository."""
    print('Please enter your commit message for this commit:')  # Added line
    user_input = input()  
    safe_user_input = shlex.quote(user_input)
    # Determine the current branch name dynamically
    current_branch_command = "git rev-parse --abbrev-ref HEAD"
    current_branch_output, current_branch_error, current_branch_exit_code = run_command(current_branch_command)
    if current_branch_exit_code != 0:
        logging.error(f"Error determining current branch: {current_branch_error}")
        return
    current_branch = current_branch_output.strip()
    logging.info(f"Current branch is {current_branch}")

    # Check if there are any changes to commit
    has_changes_command = "git status --porcelain"
    has_changes_output, has_changes_error, has_changes_exit_code = run_command(has_changes_command)
    if not has_changes_output:
        logging.info("No changes to commit.")
        return

    commands = [
        "git add .",
        f"git commit -m \"{safe_user_input}\"",
        f"git push origin {current_branch}"
    ]
    for command in commands:
        output, error, exit_code = run_command(command)
        if exit_code != 0:
            logging.error(f"Failed to execute command: {command}")
            break
        else:
            logging.info(f"Command executed successfully: {command}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    commit_and_push_changes()