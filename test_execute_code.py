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
    test2 = UI_Window()
    test2.tape_memory = Tape()
    for i in range(6):
        write(test2, test2, str(i % 2))
        move(test2, test2, ">")
    file = test2.templates_path + "/invert_values.ptm"
    import_code(test2, file)
    execute_code(test2, test2, test2.instructions, 0)
    assert test2.instructions != {} #checks if instructions
    assert test2.tape_memory.tape == ['b']*25+['1', '0', '1', '0', '1', '0']+['b']*20
