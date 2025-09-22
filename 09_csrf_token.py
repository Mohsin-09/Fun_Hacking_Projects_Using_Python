"""
09_csrf_token.py
Shows CSRF token generation and verification conceptually.
In a web app, tokens are stored in session and validated on form submission.
"""
import secrets, time

def new_token():
    return secrets.token_urlsafe(24)

if __name__ == "__main__":
    t = new_token()
    print("CSRF token (store in session):", t)
    print("Tokens should be single-use and have short expiry in production.")
