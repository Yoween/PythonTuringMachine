#!/usr/bin/env python3
# scrollable_frame.py
#
# ADAM Loris
# 30-01-2023
#==================================

import tkinter as tk

def scroll_bar(self, container, width) :
    self.canvas = tk.Canvas(container, width=int(width/9), bg='lightgrey')
    self.scrollbar = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
    self.scrollable_frame = tk.Frame(self.canvas)

    self.scrollable_frame.bind(
        "<Configure>",
        lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )
    )

    self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=int(width/6))

    self.canvas.configure(yscrollcommand=self.scrollbar.set)