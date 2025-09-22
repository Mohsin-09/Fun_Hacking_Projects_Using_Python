"""
34_error_handling.py
Shows not to leak stack traces to users; log internally and show generic messages to clients.
"""
def handle_error(e):
    # log detail internally (not printed to user)
    print("LOG:", repr(e))
    return "An internal error occurred"

if __name__ == "__main__":
    print(handle_error(ValueError("secret info")))
