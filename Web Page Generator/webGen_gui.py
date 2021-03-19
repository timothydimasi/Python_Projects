import tkinter as tk
from tkinter import *
import webbrowser

import webGen_func
import webGen_main


def load_gui(self):
    label = tk.Label(text="Text to display:")
    label.pack(pady=(20,10))

    userBody = StringVar()

    entry = tk.Entry(width=60,textvariable=userBody)
    entry.pack()

    def openPage(self):
        y = userBody.get()

        x = open("sale.html", "w")

        message = "<html><body>" + str(y) + "</body></html>"
        x.write(message)
        x.close()

        webbrowser.open_new_tab("sale.html")

    btn = tk.Button(text=("Generate Page"),command=lambda: openPage(self))
    btn.pack(pady=(25,0))






if __name__ == "__main__":
    pass

