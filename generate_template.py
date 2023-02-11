#!/usr/bin/env python3
# ganerate_template.py
#
# LAROCHE Tristan
# 31-01-2023
#==================================

from tkinter import filedialog
import tkinter as tk
import i18n

def generate_template(self):
    """Creates a window with some text and buttons then calls "template_creator"
    """
    self.generation_window = tk.Toplevel(self.root)
    self.generation_window.title(i18n.t("generate"))
    tk.Label(self.generation_window, text= i18n.t("template_text")).pack()
    self.entry = tk.Entry(self.generation_window)
    self.entry.pack()
    self.choice = tk.IntVar()
    tk.Radiobutton(self.generation_window, text=i18n.t("from_file"), variable= self.choice, value= 0).pack()
    tk.Radiobutton(self.generation_window, text=i18n.t("to_file"), variable= self.choice, value= 1).pack()
    self.go_button = tk.Button(self.generation_window, text= "Go!", command= lambda: [template_creator(self, self.entry.get(), self.choice.get())])
    self.go_button.pack()
    tk.Button(self.generation_window, text= i18n.t("quit"), command= self.generation_window.destroy).pack()
    
def template_creator(self, size: int, choice: int):
    """Opens a file and creates and empty template

    Args:
        size (int): The "size" of the template (ex: 1 = 1:b 1:0 1:1)
        choice (int): 0 to open an existing file | 1 to save as a new file
    """
    steps = ("b", "0", "1")
    try:
        if choice == 0:
            self.file = open(filedialog.askopenfilename(filetypes=[('Python Turing Machine (.ptm)', '*.ptm')]), "w")
        elif choice == 1:
            self.file = open(filedialog.asksaveasfilename(filetypes=[('Python Turing Machine (.ptm)', '*.ptm')]), "w")
    except:
        return
    for i in range(1, int(size)+1):
        for j in range(3):
            self.file.write(f"{i} : {steps[j]} : - : - : {i}\n")
    self.file.close()