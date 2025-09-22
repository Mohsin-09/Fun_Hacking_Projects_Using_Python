"""
04_xor_demo.py
Toy XOR "encryption" to show why proper cryptography libraries are necessary.
**DO NOT** use XOR for real encryption.
"""
def xor_bytes(data: bytes, key: bytes):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

if __name__ == "__main__":
    plain = b"hello world"
    key = b"key"
    c = xor_bytes(plain, key)
    print("cipher:", c)
    print("recovered:", xor_bytes(c, key))
