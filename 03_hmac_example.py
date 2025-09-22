"""
03_hmac_example.py
Demonstrates HMAC usage (message authentication) using hashlib.
"""
import hmac, hashlib

key = b"supersecretkey"
msg = b"important message"
tag = hmac.new(key, msg, hashlib.sha256).hexdigest()
print("HMAC tag:", tag)
# Verify
print("Verification ok:", hmac.compare_digest(tag, hmac.new(key,msg,hashlib.sha256).hexdigest()))
