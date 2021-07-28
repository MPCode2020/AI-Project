#!/usr/bin/env python3

# This following code is for a text based version
# of our target program. In this Ui we can also add
# a button to enable speech.

import tkinter as tk
import platform as pf
import os

class TempUI():
    def __init__(self):
        self.tkroot = tk.Tk()
        self.bg_colour = "black"
        self.fg_colour = "lightblue"

        self.tkroot.title(f"{os.getlogin()}-UI-version-chatbot")
        self.tkroot.geometry("400x400")
        self.tkroot.resizable(False, False)
        self.tkroot.configure(bg = self.bg_colour)

        self.tkroot.mainloop()
    
if __name__ == "__main__":
    UI = TempUI()
