"""
14_path_traversal.py
Demonstrates path traversal risk and a safe whitelist approach.
"""
from pathlib import Path

BASE = Path("public_files").resolve()
BASE.mkdir(exist_ok=True)

def safe_open(rel):
    candidate = (BASE / rel).resolve()
    if BASE in candidate.parents or candidate == BASE:
        return candidate.read_text()
    raise Exception("Path outside allowed directory")

if __name__ == "__main__":
    (BASE/"ok.txt").write_text("hello")
    print(safe_open("ok.txt"))
    try:
        print(safe_open("../etc/passwd"))
    except Exception as e:
        print("Blocked:", e)
