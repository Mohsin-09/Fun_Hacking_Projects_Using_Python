"""
15_logging.py
Shows structured logging and avoiding logging secrets like passwords or tokens.
"""
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("demo")
logger.info("Service started")
# never log sensitive info
