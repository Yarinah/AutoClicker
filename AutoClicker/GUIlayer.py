import tkinter as tk
from tkinter import filedialog, simpledialog
import threading
import pyautogui

from mouseClicker import mouseClickerObject


class autoClickerGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.mouse_clicker = mouseClickerObject()
        
    def create_widgets(self):
        # Interval configuration
        self.interval_label = tk.Label(self, text="Interval (seconds)")
        self.interval_label.pack()
        self.interval_entry = tk.Entry(self)
        self.interval_entry.pack()
        
        # Mouse position set
        self.set_pos_button = tk.Button(self, text="Set mouse position", command=self.set_mouse_pos)
        self.set_pos_button.pack()
        
        # Start clicking
        self.start_clicking_botton = tk.Button(self, text="Start clicking", command=self.start_clicking)
        self.start_clicking_botton.pack()
        
        # Record mouse activity
        self.record_button = tk.Button(self, text="Record mouse activity", command=self.record_mouse)
        self.record_button.pack()
        
        # Perform mouse activity
        self.perform_button = tk.Button(self, text="Perform mouse activity", command=self.perform_mouse)
        self.perform_button.pack()
        
        # Quit button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")
        
    def set_mouse_pos(self):
        self.mouse_clicker.setXY_MousePos()
        
    def start_clicking(self):
        self.mouse_clicker.setInterval(float(self.interval_entry.get()))
        self.mouse_clicker.click()
        
    def record_mouse(self):
        duration = simpledialog.askinteger("Duration", "Enter the duration of the recording")
        if duration:
            thread = threading.Thread(target=self.mouse_clicker.record_mouse_activity, args=(duration,))
            thread.start()
            
    def perform_mouse(self):
        file_path = filedialog.askopenfilename(title="Select mouse record file")
        if file_path:
            thread = threading.Thread(target=self.mouse_clicker.perform_mouse_activity, args=(file_path,))
            thread.start()
        
    
        
