"""Session 3.3 demo — logging instead of print for unattended automation."""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

log = logging.getLogger("report-bot")

log.debug("This won't show (level is INFO)")
log.info("Starting report run")
log.warning("Disk usage at 82%%")
log.error("Failed to reach mail server")

# Logging an exception with traceback
try:
    1 / 0
except ZeroDivisionError:
    log.exception("Math error while computing ratio")

log.info("Run finished")
