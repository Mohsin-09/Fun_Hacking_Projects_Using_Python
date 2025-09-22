"""
18_safe_serialization.py
Shows danger of pickle with untrusted data and recommends JSON for untrusted contexts.
"""
import pickle, json

data = {"a":1}
b = pickle.dumps(data)
print("Pickle size:", len(b))
print("JSON:", json.dumps(data))
print("Do NOT unpickle untrusted data.")
