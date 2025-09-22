"""
02_password_strength.py
Simple password strength estimator (length, classes of characters).
"""
import re

def score(p):
    s = 0
    if len(p) >= 8: s += 1
    if re.search(r"[a-z]", p): s += 1
    if re.search(r"[A-Z]", p): s += 1
    if re.search(r"\d", p): s += 1
    if re.search(r"[^A-Za-z0-9]", p): s += 1
    return s

if __name__ == "__main__":
    tests = ["password", "Password1", "P@ssw0rd!"]
    for t in tests:
        print(t, "score:", score(t))
