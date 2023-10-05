import logging
import os
from logging.handlers import TimedRotatingFileHandler

# Logging Setup
log_file = os.path.join(os.getcwd(), "static", "log_file.log")
backup_count = 2

# Creating Logs
logger = logging.getLogger("athena_logger")
logger.setLevel(logging.DEBUG)

# Creating a Time Rotating Handler
file_handler = TimedRotatingFileHandler(
    filename=log_file,
    when='midnight',
    interval=1,
    backupCount=backup_count,
    encoding='utf-8',
    delay=True
)

# Creating a format to specify the log message format
formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)
