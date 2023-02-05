# scrollable_frame.py
#
# ADAM Loris
# 30-01-2023
#==================================

import tkinter as tk

def scroll_bar(self, container, cwidth, cheight) :
    self.canvas = tk.Canvas(container, width=int(cwidth/22), bg='red')
    self.scrollbar = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
    self.scrollable_frame = tk.Frame(self.canvas, bg='yellow')

    self.scrollable_frame.bind(
        "<Configure>",
        lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )
    )

    self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

    self.canvas.configure(yscrollcommand=self.scrollbar.set)