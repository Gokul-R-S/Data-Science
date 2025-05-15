import logging
import os

# This makes sure logs are in backend dir
SERVER_LOG_FILE = os.path.join(os.path.dirname(__file__), 'server.log')
FRONTEND_LOG_FILE = os.path.join(os.path.dirname(__file__), 'frontend.log')

def setup_logger(name, log_file=SERVER_LOG_FILE, level=logging.INFO):
    logger = logging.getLogger(name)

    if logger.handlers: # Prevents duplicate FileHandlers
        return logger

    logger.setLevel(level)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def setup_frontend_logger(name):
    return setup_logger(name,log_file=FRONTEND_LOG_FILE)