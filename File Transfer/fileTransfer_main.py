import tkinter as tk
from tkinter import *
from tkinter import filedialog

import fileTransfer_gui
import fileTransfer_func


class fileTransfer(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.minsize(465,180)
        self.master.maxsize(465,180)

        fileTransfer_func.center_window(self,465,180)
        self.master.title("File Transfer Application")

        fileTransfer_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = fileTransfer(root)
    root.mainloop()   