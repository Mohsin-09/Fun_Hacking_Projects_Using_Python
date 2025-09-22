"""
05_file_handling.py
Shows secure file handling practices (avoid race conditions, use 'with').
"""
from pathlib import Path

def write_atomic(path, data):
    tmp = Path(str(path) + ".tmp")
    with tmp.open("wb") as f:
        f.write(data)
    tmp.replace(path)  # atomic on many OSes

if __name__ == "__main__":
    write_atomic("sample.bin", b"safe content")
    print("Wrote sample.bin atomically")
