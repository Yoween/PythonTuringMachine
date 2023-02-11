#!/usr/bin/env python3

from main import UI_Window
import tkinter, time
import tkinter as tk

def test_execution_tab():
    test = UI_Window()
    test.execution_tab()
    for i in test.circles.values():
        assert i in [[40, 20, 'white'], [42, 40, 'white'], [45, 60, 'white'], [49, 80, 'white'], [54, 100, 'white'], [60, 120, 'white'], [68, 140, 'white'], [78, 160, 'white'], [90, 180, 'white'], [104, 200, 'white'], [118, 220, 'white'], [136, 237, 'white'], [156, 252, 'white'], [178, 265, 'white'], [204, 270, 'white'], [228, 265, 'white'], [250, 252, 'white'], [270, 237, 'white'], [288, 220, 'white'], [304, 200, 'white'], [318, 180, 'white'], [330, 160, 'white'], [340, 140, 'white'], [348, 120, 'white'], [354, 100, 'white'], [359, 80, 'white'], [363, 60, 'white'], [366, 40, 'white'], [368, 20, 'white']]
        
    time.sleep(2)

def test_preview_tab():
    test = UI_Window()
    test.preview_tab
    for i in test.__dict__.keys():
        assert i in ['config_file', 'config', 'color_highlight', 'color_blank', 'color_zero', 'color_one', 'width', 'height', 'root', 'instructions', 'execution', 'circles', 'tape_memory', 'default_path', 'templates_path', 'menu', 'menu_file', 'menu_templates', 'menu_load_template', 'menu_languages', 'right_tab', 'canvas2', 'button_go', 'button_clear', 'button_left', 'button_right', 'current_label', 'next_label', 'button_slow', 'button_b', 'button_0', 'button_1', 'current_value', 'next_value', 'left_tab', 'canvas', 'scrollbar', 'scrollable_frame', 'text_name', 'label_state', 'label_read', 'label_write', 'label_move', 'label_new_state']
        
    time.sleep(2)

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
    
    time.sleep(2)