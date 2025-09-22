"""
41_os_command.py
Shows the risk of building shell commands by concatenation and safe alternatives.
"""
import subprocess, shlex

def unsafe(user_input):
    cmd = "echo " + user_input
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout

def safe(user_input):
    return subprocess.run(["echo", user_input], capture_output=True, text=True).stdout

if __name__ == "__main__":
    print("safe:", safe("hello; rm -rf /"))  # safe because not shell-parsed
