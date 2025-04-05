import logging
import os

LOG_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'server.log') # This makes sure logs are in backend dir

def setup_logger(name, log_file=LOG_FILE, level=logging.DEBUG):
    logger = logging.getLogger(name)

    if logger.handlers:  # Prevent duplicate handlers
        return logger

    logger.setLevel(level)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
