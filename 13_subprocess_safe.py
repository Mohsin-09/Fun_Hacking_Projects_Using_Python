"""
13_subprocess_safe.py
Demonstrates safe use of subprocess (avoid shell=True with untrusted input).
"""
import subprocess

def run_ls(path):
    # safe: pass args as list
    return subprocess.run(["ls", "-la", path], capture_output=True, text=True)

if __name__ == "__main__":
    print(run_ls(".").stdout[:400])
