import os
import logging
from datetime import datetime
import sys

"""
Utils
Utilities functions
initiate_log: Function to log create a log object
tic_tac: Timer object to log the time taken to execute the process
"""

__all__ = [
    'initiate_log',
    'tic_tac'
]

class tic_tac():
    """
    Class to represent the chosen process timer

    Attributes
    ----------
    process_name : str
        Process name to have his time measured
    dump_file : str
        Name of the file that will store the logs, by default 'experiment.log'

    Methods
    -------
    stop_watch():
        Prints the person's name and age.
    """    
    def __init__(self, process_name='default', dump_file: str = 'experiment.log'):
        self.t0 = datetime.now()
        self.tf = None
        self.process_name = process_name
        self.logger = get_logger(__name__, dump_file)
    
    def stop_watch(self):
        """
            Stops the timer and logs the time that has been taken to execute the process
        """        
        self.tf = datetime.now()
        diff = self.tf - self.t0
        self.logger.info(f"Processo: {self.process_name} - Tempo de execução: {diff}")

def initiate_log():
    "Initiates the logging object to be used"
    cwd = os.getcwd()
    path = os.path.dirname(cwd)
    projeto = os.path.basename(path)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S',
        handlers=[
            logging.FileHandler(projeto + ".log", mode='a'),
            logging.StreamHandler(sys.stdout)
        ]
    )


