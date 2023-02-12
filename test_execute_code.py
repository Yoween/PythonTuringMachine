#!/usr/bin/env python3

from execute_code import import_code, execute_code, move, write, clear_tape
from main import UI_Window
from Tape import Tape
import tkinter, time
import tkinter as tk

test = UI_Window()

def test_import_code():
    file = test.templates_path + "/invert_values.ptm"
    import_code(test, file)
    assert test.left_tab.winfo_exists() == True
    assert len(test.instructions) == 2 # length of the instructions

def test_execute_code():
    test.tape_memory = Tape()
    for i in range(6):
        write(test, test, str(i % 2))
        move(test, test, ">")
    print(test.tape_memory.tape)
    file = test.templates_path + "/invert_values.ptm"
    import_code(test, file)
    execute_code(test, test, test.instructions, 0)
    assert test.instructions != {} #checks if instructions
    time.sleep()
    test.root.destroy()
    
test_execute_code()