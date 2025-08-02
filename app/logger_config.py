import logging
import os

def setup_logger(name: str, level=logging.INFO, log_to_file: bool = FALSE):
    
    """
    Return logger with a given name and level

    Args:
        name (str): Name of the logger (usually use __name__)
        level (int): Logging level (i.e., logging,DEBUG, logging.INFO)
        log_to_file (bool): Whether to also log to a file ('log/app.log')

    Returns:
        logging.Logger: A ready to use logger object
    """

    # Create a logger with a specified name
    logger = logging.getLogger(name)

    # Set the logging level (i.e. INFO)
    logger.setLevel(level)

    

