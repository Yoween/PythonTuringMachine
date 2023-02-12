#!/usr/bin/env python3os

from main import UI_Window
import tkinter, os, json
test = UI_Window()

def test_execution_tab():
    test.execution_tab()
    for i in test.circles.values():
        assert i in [[40, 20, 'white'], [42, 40, 'white'], [45, 60, 'white'], [49, 80, 'white'], [54, 100, 'white'], [60, 120, 'white'], [68, 140, 'white'], [78, 160, 'white'], [90, 180, 'white'], [104, 200, 'white'], [118, 220, 'white'], [136, 237, 'white'], [156, 252, 'white'], [178, 265, 'white'], [204, 270, 'white'], [228, 265, 'white'], [250, 252, 'white'], [270, 237, 'white'], [288, 220, 'white'], [304, 200, 'white'], [318, 180, 'white'], [330, 160, 'white'], [340, 140, 'white'], [348, 120, 'white'], [354, 100, 'white'], [359, 80, 'white'], [363, 60, 'white'], [366, 40, 'white'], [368, 20, 'white']]

def test_preview_tab():
    test.preview_tab
    for i in test.__dict__.keys():
        assert i in ['config_file', 'config', 'color_highlight', 'color_blank', 'color_zero', 'color_one', 'width', 'height', 'root', 'instructions', 'execution', 'circles', 'tape_memory', 'default_path', 'templates_path', 'menu', 'menu_file', 'menu_templates', 'menu_load_template', 'menu_languages', 'right_tab', 'canvas2', 'button_go', 'button_clear', 'button_left', 'button_right', 'current_label', 'next_label', 'button_slow', 'button_b', 'button_0', 'button_1', 'current_value', 'next_value', 'left_tab', 'canvas', 'scrollbar', 'scrollable_frame', 'text_name', 'label_state', 'label_read', 'label_write', 'label_move', 'label_new_state']

def test_new_state():
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

def test_scroll_bar():
    test = UI_Window()
    assert type(test.instructions) == dict
    assert type(test.execution) == tuple
    assert type(test.circles) == dict
    assert test.canvas.winfo_exists() == 1 and type(test.canvas) == tkinter.Canvas
    assert test.scrollbar.winfo_exists() == 1 and type(test.scrollbar) == tkinter.Scrollbar
    assert test.scrollable_frame.winfo_exists() == 1 and type(test.scrollable_frame) == tkinter.Frame

def test_change_language():
    config = ""
    config_file = os.getcwd() + "/config.json"
    with open(config_file, "r") as f:
        config = json.load(f) #backs up values
    value = ""
    if config["language"] == "fr":
        value = "en"
    elif config["language"] == "en":
        value = "fr"
    test.change_language(value)
    with open(config_file, "r") as f:
        config_new = json.load(f) #checks if worked
        assert config_new["language"] != config["language"]

def test_change_colors():
    config = ""
    config_file = os.getcwd() + "/config.json"
    with open(config_file, "r") as f:
        config = json.load(f) #backs up values
    test.change_colors("red", "blue", "green", "white") #changes values
    with open(config_file, "r") as f:
        config_new = json.load(f)
    for i in ["red", "blue", "green", "white"]:
        assert i in config_new.values()
    #restore values
    test.change_colors(config["color_highlight"], config["color_blank"], config["color_zero"], config["color_one"])
    with open(config_file, "r") as f:
        config_check = json.load(f) #backs up values
    for i in config_check.values():
        assert i in config.values() #checks if correctly restored

def test_config_editor():
    test.config_editor()
    assert type(test.config_window) is tkinter.Toplevel

def test_restart():
    test.restart()
    assert type(test.restart_window) is tkinter.Toplevel

def test___init__():
    test = UI_Window()
    assert test.root.winfo_width() == 800
    assert test.root.winfo_height() == 380
    assert test.menu.winfo_exists() == 1
    assert test.menu_file.winfo_exists() == 1
    assert test.menu_templates.winfo_exists() == 1
    assert test.menu_load_template.winfo_exists() == 1
    assert test.menu_languages.winfo_exists() == 1
