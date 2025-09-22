"""
01_hashing.py
Demonstrates secure hashing of passwords using hashlib + salt (secrets).
Never store plain text passwords.
"""
import hashlib, secrets

def hash_password(password: str, salt: bytes = None):
    if salt is None:
        salt = secrets.token_bytes(16)
    h = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000)
    return salt.hex(), h.hex()

if __name__ == "__main__":
    pwd = "correcthorsebatterystaple"
    salt, digest = hash_password(pwd)
    print("Salt:", salt)
    print("Digest:", digest)
