import subprocess
import logging
import shlex

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def run_command(command):
    """Runs a shell command and returns the output, error and exit code."""
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        output, error = process.communicate()
        if error:
            logging.error(f"Error running command '{command}': {error}")
        return output, error, process.returncode
    except Exception as e:
        logging.error(f"Error running command '{command}': {e}", exc_info=True)
        return None, str(e), 1


def git_status():
    """Check for uncommitted changes in the workspace."""
    command = "git status --porcelain"
    output, error, exit_code = run_command(command)
    if exit_code != 0:
        logging.error(f"Error checking git status: {error}")
        return False
    if output:
        logging.info("Uncommitted changes detected.")
        return True
    else:
        logging.info("No uncommitted changes detected.")
        return False


def commit_and_push():
    """Commits and pushes changes to the remote repository."""
    user_input = input("Enter your commit message: All changes")  # INPUT_REQUIRED {Enter a meaningful commit message}
    safe_user_input = shlex.quote(user_input)
    commands = [
        "git add .",
        f"git commit -m {safe_user_input}",
        "git push origin master"
    ]
    for command in commands:
        output, error, exit_code = run_command(command)
        if exit_code != 0:
            logging.error(f"Error running '{command}': {error}", exc_info=True)
            break
        else:
            logging.info(f"Successfully executed: {command}")


if __name__ == "__main__":
    if git_status():
        commit_and_push()
    else:
        logging.info("No changes to commit.")