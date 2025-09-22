"""
19_secure_random.py
Shows use of secrets module for cryptographic randomness vs random module.
"""
import secrets, random
print("secrets token:", secrets.token_hex(8))
print("random randrange (not for crypto):", random.randrange(1,100))
