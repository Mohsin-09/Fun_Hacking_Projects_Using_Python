"""
30_token_revocation.py
Simple example showing token revocation list for JWT-like tokens (simulation).
"""
revoked = set()
def revoke(token):
    revoked.add(token)
def is_revoked(token):
    return token in revoked

if __name__ == "__main__":
    t = "tok123"
    print("revoked?", is_revoked(t))
    revoke(t)
    print("revoked?", is_revoked(t))
