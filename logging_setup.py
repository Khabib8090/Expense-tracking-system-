

import logging

def setup_logger(name,log_file="server.log",level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    file_handler= logging.FileHandler(log_file) # is naam se save hogi 

    formatter= logging.Formatter("%(asctime)s - %(levelname)s -%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler) #"Logger ko bola: ye file handler le lo, aur isko use karke sab messages my_app.log mein likhna start karo."
    
    return logger



