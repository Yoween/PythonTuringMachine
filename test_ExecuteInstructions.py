#!/usr/bin/env python3
from ExecuteInstructions import ExecuteInstructions
from main import UI_Window
from execute_code import import_code
import tkinter as tk


def test_process():
    import os
    test = ExecuteInstructions()
    read = ("b", "0", "1")
    path = os.getcwd() + "/default_templates/add_one_binary.ptm"
    result = test.process(path)
    assert result == {'1': {'b': ('-', '<', '1'), '0': ('-', '-', '2'), '1': ('-', '-', '2')}, '2': {'b': ('-', '-', 'f'), '0': ('1', '>', '2'), '1': ('-', '-', '3')}, '3': {'b': ('-', '-', '3'), '0': ('-', '-', '3'), '1': ('0', '<', '4')}, '4': {'b': ('1', '-', '5'), '0': ('1', '-', '5'), '1': ('-', '-', '4')}, '5': {'b': ('-', '-', 'f'), '0': ('-', '>', '5'), '1': ('-', '>', '5')}}
    assert type(result) == dict
    for key in range(1, len(result)):
        assert type(result[str(key)]) == dict
        for key2 in read :
            assert type(result[str(key)][str(key2)]) == tuple and len(result[str(key)][str(key2)]) == 3

    path = os.getcwd() + "/default_templates/invert_values.ptm"
    result = test.process(path)
    assert result == {'1': {'b': ('-', '<', '1'), '0': ('-', '-', '2'), '1': ('-', '-', '2')}, '2': {'b': ('-', '-', 'f'), '0': ('1', '<', '2'), '1': ('0', '<', '2')}, '3': {'b': ('-', '-', '3'), '0': ('-', '-', '3'), '1': ('0', '<', '4')}, '4': {'b': ('1', '-', '5'), '0': ('1', '-', '5'), '1': ('-', '-', '4')}, '5': {'b': ('-', '-', 'f'), '0': ('-', '>', '5'), '1': ('-', '>', '5')}}
    assert type(result) == dict
    for key in range(1, len(result)):
        assert type(result[str(key)]) == dict
        for key2 in read :
            assert type(result[str(key)][str(key2)]) == tuple and len(result[str(key)][str(key2)]) == 3

    path = os.getcwd() + "/default_templates/remove_one_binary.ptm"
    result = test.process(path)
    assert result == {'1': {'b': ('-', '<', '1'), '0': ('-', '-', '2'), '1': ('-', '-', '2')}, '2': {'b': ('-', '-', '2'), '0': ('-', '-', '3'), '1': ('0', '>', 'f')}, '3': {'b': ('-', '-', '3'), '0': ('1', '<', '3'), '1': ('0', '<', '5')}, '4': {'b': ('-', '-', 'f'), '0': ('-', '>', '4'), '1': ('-', '>', '4')}, '5': {'b': ('-', '>', '6'), '0': ('-', '-', '4'), '1': ('-', '-', '4')}, '6': {'b': ('-', '-', '6'), '0': ('b', '>', '6'), '1': ('-', '-', '6')}}
    assert type(result) == dict
    for key in range(1, len(result)):
        assert type(result[str(key)]) == dict
        for key2 in read :
            assert type(result[str(key)][str(key2)]) == tuple and len(result[str(key)][str(key2)]) == 3

def test_is_valid():
    test = ExecuteInstructions()
    characters = ("1", "b", "g", ">", "2")
    assert test.is_valid(characters, 5) == False
    assert test.error == "Invalid character at line 5"
    characters = ("1", "b", "-", "-1", "2")
    assert test.is_valid(characters, -1) == False
    assert test.error == "Invalid character at line -1"
    characters = ("1", "b", "-", "2")
    assert test.is_valid(characters, 1) == False
    assert test.error == "Missing instructions at line 1"
    characters = ("1", "b", "-", ">", "2")
    assert test.is_valid(characters, 5) == True

def test_is_complete():
    test = ExecuteInstructions()
    instructions = {"1": {"b": ("1", "b", "g", ">", "2"), "0": ("1", "b", "g", ">", "2"), "1": ("1", "b", "g", ">", "2")}}
    assert test.is_complete(instructions) == True
    instructions = {}
    assert test.is_complete(instructions) == False
