#!/usr/bin/env python3
# ReadInstructions.py
# 
# LAROCHE Tristan
# 21-12-2022
#==================================

import logging
from Tape import Tape
from time import sleep
import tkinter as tk

class ExecuteInstructions():
    allowed_characters = ("b", ">", "<", "f", "-")
    instructions = {}
    """
    A class that takes instructions, format them in a list where 
    every character is an item then call executes them
    """
    def process(self, file_path:str):
        self.file_path = file_path
        with open(file_path) as _file:
            i = 1
            for line in _file:
                line = line.replace(" ", "").replace("\n", "")
                characters = line.split(":")

                if self.is_valid(characters, i):
                    if characters[0] not in self.instructions.keys() :
                        self.instructions[characters[0]] = {}
                    self.instructions[characters[0]][characters[1]] = (characters[2], characters[3], characters[4])
                else :
                    return (self.error)
                i += 1
            if self.is_complete(self.instructions) == False:
                return (self.error)
        return (self.instructions) 

    def is_valid(self, characters:list, line:int):
        """
        Checks if characters are valid

        Args:
            characters {list}: a formatted list with the instructions
            line  {int}: just the line we're processing

        Returns:
            bool: True is characters are valid otherwise false
        """
        if len(characters) < 5:
                self.error = f"Missing instructions at line {line}"
                logging.basicConfig(filename="latest.log", level=logging.INFO)
                logging.error(self.error)
                return False
        for index in range(len(characters)):
            if characters[index].lower() in self.allowed_characters or (characters[index].isdigit() and int(characters[index]) >= 0):
                pass
            else:
                self.error = f"Invalid character '{characters[index]}' at index {index + 1}, line {line}"
                logging.basicConfig(filename="latest.log", level=logging.INFO)
                logging.error(self.error)
                return False
        return True

    def is_complete(self, instructions:dict):
        for i in range(1, len(instructions) + 1):
            if len(instructions[str(i)]) != 3:
                self.error = f"Missing instructions line"
                logging.basicConfig(filename="latest.log", level=logging.INFO)
                logging.error(self.error)
                return False


    def start(self, ui, instructions:dict, tape_memory = Tape(), delay = 0):
        """Executes the program when called. Used instead of '__init__' so we can decide when to start it. The core of the program, which executes instructions as a Turing machine would do.

        Args:
            instructions (dict): Contains every instructions of the program loaded.
            tape_memory (class): The tape where data are written. Here it isn't optionnal but written as so for my text editor to understand what objects are used
            delay (int, optional): The delay used for the slowed down execution. Defaults to 0.
        """
        iterations = len(instructions)
        self.current_state = "1"
        while iterations > 0:
            tape_index = tape_memory.get_position()
            tape_index_value = tape_memory.read(tape_index)
                
            sub_insruction = instructions[self.current_state][tape_index_value]
            if sub_insruction[0] == "-":
                tape_memory.write(tape_index, tape_index_value)
            else :
                tape_memory.write(tape_index, sub_insruction[0])
                
            if sub_insruction[1] != "-":
                tape_memory.move(sub_insruction[1])
                
            if sub_insruction[2] == "f":
                iterations = 0
            else:
                previous_state = self.current_state
                self.current_state = sub_insruction[2]
                if previous_state != self.current_state:
                    iterations -= 1
            sleep(delay)
            print(tape_memory.tape)