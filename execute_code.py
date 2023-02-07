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

def execute_code(self, selfe, instructions: dict, delay):
    """Starts the programs with the properly formatted file. Called by 'import_code'.

    Args:
        instructions (dict): Contains every instructions of the program loaded.
    """
    if instructions == {}:
        return
    self.execution.start(selfe, instructions, self.tape_memory, delay)

def move(self, direction: str):
    """Moves left or right on the 'tape' (tape_memory.tape) based on the parameter.

    Args:
        direction (str): '<' or '>' for the direction.
    """
    if self.execution == ():
        return
    self.tape_memory.move(direction)

def write(self, value: str):
    """Writes a value on the 'tape' (tape_memory.tape) based on the parameter.

    Args:
        value (str): 'b', '0' or '1' for the values to write.
    """
    if self.execution == ():
        return
    self.tape_memory.write(self.tape_memory.get_position(), value)
    print(self.tape_memory.tape)

def clear_tape(self):
    """Clears the 'tape' (tape_memory) by instantiating the class again. The previous tape will be left unused and eventually discarded by the garbage collector.
    """
    self.tape_memory = Tape()
    print(self.tape_memory.tape)