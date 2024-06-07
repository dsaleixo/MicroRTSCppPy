import datetime
import logging
import os
import sys




class StdoutLogger:

    logger = None

    @classmethod
    def init_logger(cls,id :str) -> None:

        output_folder = os.path.join('output', 'logs')
        os.makedirs(output_folder, exist_ok=True)

        
        filename = f'out_{id}.txt'
        log_handlers = [
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(os.path.join(output_folder, filename), mode='w')
        ]
        
        logging.basicConfig(handlers=log_handlers, format='%(asctime)s: %(message)s', level=logging.DEBUG)
        cls.logger = logging.getLogger()
        
    @classmethod
    def log(cls, sender: str, message: str, level: str = 'info') -> None:
        
        if level == 'info':
            cls.logger.info(f'[{sender}] {message}')
