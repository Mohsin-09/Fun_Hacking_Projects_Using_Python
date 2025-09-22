"""
16_config_env.py
Shows reading secrets from environment variables (NOT checked into source).
"""
import os
secret = os.getenv("APP_SECRET", "<set APP_SECRET in env>")
print("Secret (do not print in production):", secret)
