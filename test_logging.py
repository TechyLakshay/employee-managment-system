#!/usr/bin/env python3
"""Quick test to verify logging is working"""

from app.observability.logger import setup_logging, get_logger

# Setup logging
setup_logging()

# Get logger
logger = get_logger("test")

# Log messages
logger.info("✅ Testing INFO log - should appear in console AND app/logs/app.log")
logger.error("❌ Testing ERROR log - should appear in console AND app/logs/app.log")
logger.debug("🔍 Testing DEBUG log - should NOT appear (level=INFO)")

print("\n✨ Check app/logs/app.log to verify logs were written!")
