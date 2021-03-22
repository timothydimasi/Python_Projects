import tkinter as tk
from tkinter import *
from tkinter import filedialog
import shutil
import os
import time

import fileTransfer_func


def load_gui(self):

    # will start by loading the two browse buttons
    btnBrowse1 = tk.Button(text=("Browse"),command=lambda: srcFolder(self))
    btnBrowse1.grid(row=1,column=0,padx=(20,0))

    btnBrowse2 = tk.Button(text=("Browse"),command=lambda: destFolder(self))
    btnBrowse2.grid(row=3,column=0,padx=(20,0))

    # these functions pertain to the entry fields below
    # I want to see if I can keep functions like these in a separate doc
    # but it seems like 'textvariable' will only accept local variables
    source = StringVar()
    destination = StringVar()
    
    def srcFolder(self):
        selection = filedialog.askdirectory()
        source.set(selection)

    def destFolder(self):
        selection = filedialog.askdirectory()
        destination.set(selection)


    # next I will load the entry and label widgets for the selected folders
    labelSource = tk.Label(text=("Source Folder:"))
    labelSource.grid(row=0,column=1,pady=(10,0))
    entrySource = tk.Entry(width=60,textvariable=source)
    entrySource.grid(row=1,column=1,padx=(20,0))

    labelDest = tk.Label(text=("Destination Folder:"))
    labelDest.grid(row=2,column=1)
    entryDest = tk.Entry(width=60,textvariable=destination)
    entryDest.grid(row=3,column=1,padx=(20,0))


    # lastly, the 'initiate' button
    btnInitiate = tk.Button(text=("Initiate"),width=12,height=2,command=lambda: initiate(self))
    btnInitiate.grid(row=4,column=1,sticky=W,padx=(145,0),pady=(10,0))

    def initiate(self):
        secondsInDay = 86400

        # I tried this without using '.get()' and it wasn't allowing me to use stringvar data types
        sourceFolder = source.get()
        destinationFolder = destination.get()

        now = time.time()
        before = now - secondsInDay

        def last_mod_time(files):
            return os.path.getmtime(files)
        
        for files in os.listdir(sourceFolder):
            source_fpath = os.path.join(sourceFolder, files)
            if last_mod_time(source_fpath) > before:
                destination_fpath = os.path.join(destinationFolder, files)
                shutil.move(source_fpath, destination_fpath)




if __name__ == "__main__":
    pass



