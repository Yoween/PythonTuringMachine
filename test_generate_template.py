#!/usr/bin/env python3

from main import UI_Window
from generate_template import generate_template, template_creator
import tkinter, os, time
import tkinter as tk

def test_generate_template():
    current_dir = os.getcwd()
    test_file = current_dir + "/test_program.ptm"
    open(test_file, "x") #create temp file for test
    
    test = UI_Window()
    generate_template(test)
    assert type(test.generation_window) == tkinter.Toplevel
    assert type(test.go_button) == tkinter.Button
    test.entry.insert(0, 2) #sets length to 2
    test.choice = tkinter.IntVar(test.root, value=2)
    test.file = open(test_file, "w")
    test.go_button.invoke() #call the function to create file

    with open(test_file, "r") as file:
        assert len(file.read()) == 108 #checks if good length: 2 * 3 * (5 + 4 + 8 + 1): length * 3 * (number of instructions + number of separators + number of whitespaces + 1 return char)
        
    os.remove(current_dir + "/test_program.ptm")
    
    time.sleep(2)

def test_template_creator():
    current_dir = os.getcwd()
    test_file = current_dir + "/test_program.ptm"
    open(test_file, "x") #create temp file for test
    
    test = UI_Window()
    test.file = open(test_file, "w")
    template_creator(test, 3, 2)
    
    with open(test_file, "r") as file:
        assert len(file.read()) == 162 #checks if good length: 3 * 3 * (5 + 4 + 8 + 1): length * 3 * (number of instructions + number of separators + number of whitespaces + 1 return char)
        
    os.remove(current_dir + "/test_program.ptm")
    
    time.sleep(2)