import tkinter as tk
from tkinter import *

import webGen_func
import webGen_gui


class webGen(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(465,180)
        self.master.maxsize(465,180)

        webGen_func.center_window(self,465,180)
        self.master.title("Web Page Generator")

        webGen_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = webGen(root)
    root.mainloop()