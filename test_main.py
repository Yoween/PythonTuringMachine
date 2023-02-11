#!/usr/bin/env python3

from main import UI_Window
import tkinter as tk
import tkinter as tkinter

def test_new_state():
    test = UI_Window()
    instructions = {"1": {"b": "test", "0": "test", "1": "test"}}

    test.new_state(instructions["1"])
    assert type(test.__dict__[f"label_state1"]) == tkinter.Label

    assert type(test.__dict__[f"label_read1_b"]) == tkinter.Label 
    assert type(test.__dict__[f"label_read1_0"]) == tkinter.Label
    assert type(test.__dict__[f"label_read1_1"]) == tkinter.Label

    assert type(test.__dict__[f"label_write1_b"]) == tkinter.Label
    assert type(test.__dict__[f"label_write1_0"]) == tkinter.Label
    assert type(test.__dict__[f"label_write1_1"]) == tkinter.Label

    assert type(test.__dict__[f"label_move1_b"]) == tkinter.Label
    assert type(test.__dict__[f"label_move1_0"]) == tkinter.Label
    assert type(test.__dict__[f"label_move1_1"]) == tkinter.Label

    assert type(test.__dict__[f"label_new_state1_b"]) == tkinter.Label
    assert type(test.__dict__[f"label_new_state1_0"]) == tkinter.Label
    assert type(test.__dict__[f"label_new_state1_1"]) == tkinter.Label

    test.new_state(instructions["1"])
    assert type(test.__dict__[f"label_state2"]) == tkinter.Label

    assert type(test.__dict__[f"label_read2_b"]) == tkinter.Label 
    assert type(test.__dict__[f"label_read2_0"]) == tkinter.Label
    assert type(test.__dict__[f"label_read2_1"]) == tkinter.Label

    assert type(test.__dict__[f"label_write2_b"]) == tkinter.Label
    assert type(test.__dict__[f"label_write2_0"]) == tkinter.Label
    assert type(test.__dict__[f"label_write2_1"]) == tkinter.Label

    assert type(test.__dict__[f"label_move2_b"]) == tkinter.Label
    assert type(test.__dict__[f"label_move2_0"]) == tkinter.Label
    assert type(test.__dict__[f"label_move2_1"]) == tkinter.Label

    assert type(test.__dict__[f"label_new_state2_b"]) == tkinter.Label
    assert type(test.__dict__[f"label_new_state2_0"]) == tkinter.Label
    assert type(test.__dict__[f"label_new_state2_1"]) == tkinter.Label
