# This is the logger agent that will be used to log the data from the AutoClicker
# This class will be used to log the data from the AutoClicker for debugging purposes


import os
from datetime import datetime
import inspect


class Logger:
    def __init__(self):
        # Create log file
        self.directory = 'logs'
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"autoclicker_log_{time_stamp}"
        self.file_path = os.path.join(self.directory, file_name)
        
    def info(self, message: str):
        # Get the script name from the call stack
        caller_frame = inspect.stack()[1]
        script_name = os.path.basename(caller_frame.filename)
                                       
        message = f"{script_name} - [INFO] {message}"
        print(message)
        with open(self.file_path, 'a') as file:
            file.write(f"{message}\n")
            file.close()
            
    def error(self, message: str):
        # Get the script name from the call stack
        caller_frame = inspect.stack()[1]
        script_name = os.path.basename(caller_frame.filename)
                                       
        message = f"{script_name} - [ERROR] {message}"
        print(message)
        with open(self.file_path, 'a') as file:
            file.write(f"{message}\n")
            file.close()
            



