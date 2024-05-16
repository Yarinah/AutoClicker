import pyautogui
import time


class autoClickerObject:
    def __init__(self, x, y, interavl):
        self.x = x
        self.y = y
        self.interval = interavl

    def getInterval(self):
        return self.interval
    
    def setInterval(self, interval):
        self.interval = interval
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getCords(self):
        return(pyautogui.position())
        
    def click(self):
        pyautogui.click(x=self.x, y=self.y)
        time.sleep(self.interval)
        

