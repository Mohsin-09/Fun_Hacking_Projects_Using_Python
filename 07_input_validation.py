"""
07_input_validation.py
Shows whitelisting vs blacklisting input validation approach.
"""
import re

def is_valid_username(u):
    return re.fullmatch(r"[A-Za-z0-9_]{3,20}", u) is not None

if __name__ == "__main__":
    tests = ["normal_user", "bad;user", "x"*30]
    for t in tests:
        print(t, is_valid_username(t))
