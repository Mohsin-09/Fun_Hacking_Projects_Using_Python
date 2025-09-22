"""
10_rate_limit.py
Simulates simple in-memory rate limiting per user (token-bucket-ish).
Not suitable for distributed systems; concept demo only.
"""
import time, collections

class SimpleRateLimiter:
    def __init__(self, calls, per_seconds):
        self.calls = calls
        self.per = per_seconds
        self.store = collections.defaultdict(list)
    def allow(self, key):
        now = time.time()
        arr = [t for t in self.store[key] if now - t < self.per]
        arr.append(now)
        self.store[key] = arr
        return len(arr) <= self.calls

if __name__ == "__main__":
    rl = SimpleRateLimiter(3, 10)
    for i in range(5):
        print(i, "allowed?", rl.allow("user1"))
