from ast import Try
import os
import pathlib
import pyautogui
import time
from datetime import datetime


class mouseClickerObject:
    def __init__(self, interavl: float = 0.1, left_click: bool = True):
        self.x , self.y = pyautogui.position()
        self.interval = interavl
        self.left_click = left_click

    def getInterval(self):
        return self.interval
    
    def setInterval(self, interval):
        self.interval = interval
        
    def getMouseClick(self):
        return self.left_click
    
    def setMouseClick(self, left_click: bool):
        self.left_click = left_click
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getMousePos(self):
        return(pyautogui.position())
    
    def setXY_MousePos(self):
        self.x, self.y = pyautogui.position()
        
    def click(self, duration: int = None):
        if duration:
            start_time = time.time()
            while time.time() - start_time < duration:
                try:
                    pyautogui.click(x=self.x, y=self.y, interval=self.interval, button='left' if self.left_click else 'right')
                except KeyboardInterrupt:
                    print("Clicking stopped")
        else:
            try:
                pyautogui.click(x=self.x, y=self.y, interval=self.interval, button='left' if self.left_click else 'right')
            except KeyboardInterrupt:
                print("Clicking stopped")
        
    def record_mouse_activity(self, duration: int = 30):
        # Ensure the diractory exist
        directory = 'mouse_records'
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        # Create a file path with a time stamp
        time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"mouse_date_{time_stamp}"
#        file_path = pathlib.Path(directory) / file_name
        file_path = os.path.join(directory, file_name)

        start_time = time.time()
        mouse_data = []
        try:
            while True:
                # Check if the duration has elapsed
                if time.time() - start_time > duration:
                    break
                # Record mouse position and Click states
                pos = pyautogui.position()
                left_click = pyautogui.mouseDown(button='left')
                right_click = pyautogui.mouseDown(button='right')
                mouse_data.append((pos, left_click, right_click))
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("Recording stopped")
            
        # Save the data to a file
        with open(file_path, 'w') as file:
            for data in mouse_data:
                file.write(f"{data}\n")
                
        print(f"Data saved to {file_path}")
        
    def perform_mouse_actions(self, file_path: str):
        try:
            # Read the data from the file
            with open(file_path, 'r') as f:
                mouse_data = f.readlines()
            
            for data_line in mouse_data:
                data = eval(data_line.strip())
                pos = data[0]
                left_click = data[1]
                right_click = data[2]
            
            # Perform the mouse actions
            pyautogui.moveTo(pos[0], pos[1])
            if left_click:
                pyautogui.click(button='left')
            if right_click:
                pyautogui.click(button='right')
                
            time.sleep(0.1)
            
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"An error occured: {e}")

        
   
        


