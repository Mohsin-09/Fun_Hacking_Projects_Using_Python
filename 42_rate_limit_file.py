"""
42_rate_limit_file.py
Very simple file-based counter for rate limiting (demo). Not production-ready.
"""
import time, json, os
fn = "rl.json"
data = {}
if os.path.exists(fn):
    data = json.loads(open(fn).read())
u = "user1"
now = time.time()
data.setdefault(u, []).append(now)
# only keep last 60 seconds
data[u] = [t for t in data[u] if now - t < 60]
open(fn,"w").write(json.dumps(data))
print("count for", u, len(data[u]))
