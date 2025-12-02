import logging
from pathlib import Path

from config.settings import LOG_DIR

# Initialize logger.
def get_logger(name: str) -> logging.Logger:
    LOG_DIR.mkdir(exist_ok=True) # Ensure log directory exists.
    logger = logging.getLogger(name) # Create or get the logger.
    # Avoid adding multiple handlers to the logger.
    if logger.handlers:
        return logger
    
    # Set logger level and add file handler.
    logger.setLevel(logging.INFO)
    
    # Create file handler for logging to a file.
    file_handler = logging.FileHandler(Path(LOG_DIR, "test_run.log"))
    
    # Define log message format.
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s" # Log message format.
    )
    file_handler.setFormatter(formatter) # Set formatter for the file handler.
    logger.addHandler(file_handler) # Add file handler to the logger.
    return logger
