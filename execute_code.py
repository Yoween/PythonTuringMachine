#!/usr/bin/env python3
# execute_code.py
#
# LAROCHE Tristan
# 31-01-2023
#==================================

from ExecuteInstructions import ExecuteInstructions
from Tape import Tape
import tkinter as tk
import tkinter.filedialog as fd

def import_code(self, file=""):
    """Imports file if specified otherwise asks to opens one then starts the program

    Args:
        file (str, optional): The path of the file you want to open, used to load templates. Defaults to "" for nothing.
    """
    if file == "":
        open_file = fd.askopenfilename(filetypes=[('Python Turing Machine (.ptm)', '*.ptm')])
    else:
        open_file = file

    if open_file == "":
        return
    
    self.preview_tab()
    self.instructions.clear()
    self.execution = ExecuteInstructions()
    self.instructions = self.execution.process(open_file)

    if type(self.instructions) is str:
        self.error_window = tk.Toplevel(self.root)
        self.error_window.title("Error")
        tk.Label(self.error_window, text= self.instructions).pack()
        tk.Button(self.error_window, text= "Quit!", command= self.error_window.destroy).pack()

    for i in self.instructions.keys():
        self.new_state(self.instructions[i])

def execute_code(self, ui, instructions: dict, delay):
    """Starts the programs with the properly formatted file. Called by 'import_code'.

    Args:
        instructions (dict): Contains every instructions of the program loaded.
    """
    if instructions == {}:
        return
    self.execution.start(ui, instructions, self.current_value, self.next_value, self.tape_memory, delay)

def move(self, ui, direction: str):
    """Moves left or right on the 'tape' (tape_memory.tape) based on the parameter.

    Args:
        direction (str): '<' or '>' for the direction.
    """
    if self.execution == ():
        return
    self.tape_memory.move(ui, direction)

def write(self, ui, value: str):
    """Writes a value on the 'tape' (tape_memory.tape) based on the parameter.

    Args:
        value (str): 'b', '0' or '1' for the values to write.
    """
    if self.execution == ():
        return
    self.tape_memory.write(ui, self.tape_memory.get_position(), value)

def clear_tape(self, ui):
    """Clears the 'tape' (tape_memory) by instantiating the class again. The previous tape will be left unused and eventually discarded by the garbage collector.
    """
    self.tape_memory = Tape()
    self.circles = {'14': [40, 20, 'white'], '13': [42, 40, 'white'], '12': [45, 60, 'white'], '11': [49, 80, 'white'], '10': [54, 100, 'white'],
                    '9': [60, 120, 'white'], '8': [68, 140, 'white'], '7': [78, 160, 'white'], '6': [90, 180, 'white'], '5': [104, 200, 'white'],
                    '4': [120, 220, 'white'], '3': [138, 240, 'white'], '2': [158, 260, 'white'], '1': [180, 270, 'white'], '0': [204, 275, 'white'],
                    '-1': [228, 270, 'white'], '-2': [250, 260, 'white'], '-3': [270, 240, 'white'], '-4':[288, 220, 'white'], '-5': [304, 200, 'white'],
                    '-6': [318, 180, 'white'], '-7': [330, 160, 'white'], '-8': [340, 140, 'white'], '-9': [348, 120, 'white'], '-10': [354, 100, 'white'],
                    '-11': [359, 80, 'white'], '-12': [363, 60, 'white'], '-13': [366, 40, 'white'], '-14': [368, 20, 'white']}
    ui.canvas2.destroy()
    ui.canvas2 = tk.Canvas(ui.right_tab, height=310,  bg='AntiqueWhite2')
    ui.canvas2.grid(row=2, column=0, columnspan=10, sticky='nesw')
    for value in ui.circles.values() :
        ui.drawcircle(ui.canvas2, value[0], value[1], 6, value[2])