"""
11_bruteforce_sim.py
Simulates failed login attempts and account lockout defense.
"""
from collections import defaultdict
import time

attempts = defaultdict(int)
locked_until = {}

def attempt(username, ok):
    now = time.time()
    if username in locked_until and now < locked_until[username]:
        return "locked"
    if ok:
        attempts[username] = 0
        return "success"
    attempts[username] += 1
    if attempts[username] >= 5:
        locked_until[username] = now + 60  # lock for 60s
        attempts[username] = 0
        return "locked"
    return "failed"

if __name__ == "__main__":
    for i in range(7):
        print(i, attempt("alice", False))
