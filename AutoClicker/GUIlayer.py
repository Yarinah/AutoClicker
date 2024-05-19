import tkinter as tk
from tkinter import filedialog, simpledialog
import threading

from mouseClicker import mouseClickerObject


class autoClickerGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.mouse_clicker = mouseClickerObject()
        
        self.update_mouse_pos()
        self.master.bind("s", self.set_mouse_pos)
        
    def create_widgets(self):
        self.info = tk.Label(self, text="S = set mouse position")

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
        
        # Real time mouse position
        self.mouse_pos_label = tk.Label(self, text="Mouse position")
        self.mouse_pos_label.pack()
        self.mouse_pos = tk.Label(self, text="")
        self.mouse_pos.pack()
        
        # Choosen mouse position
        self.choosen_mouse_pos = tk.Label(self, text="")
        self.choosen_mouse_pos.pack()
        
                
    def get_mouse_pos(self):
        return self.mouse_clicker.getMousePos()
    
    def set_mouse_pos(self):
        self.mouse_clicker.setXY_MousePos()
        self.choosen_mouse_pos["text"] = self.get_mouse_pos()

    def update_mouse_pos(self):
        self.mouse_pos["text"] = self.get_mouse_pos()
        self.after(100, self.update_mouse_pos)
        
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
        
    
        
