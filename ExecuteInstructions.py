#!/usr/bin/env python3
# ReadInstructions.py
# 
# LAROCHE Tristan
# 21-12-2022
#==================================

import logging, i18n
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
        values_read = ("b", "0", "1")
        values_move = (">", "<")
        if len(characters) < 5:
                self.error = f"Missing instructions at line {line}"
                logging.basicConfig(filename="latest.log", level=logging.INFO)
                logging.error(self.error)
                return False
        if (characters[0].isdigit() and int(characters[0]) > 0) and (characters[1] in values_read) and (characters[2] in values_read) and (characters[3] in values_move) and (characters[4].isdigit() and int(characters[4]) > 0):
            pass
        else:
            self.error = f"Invalid character at line {line}"
            logging.basicConfig(filename="latest.log", level=logging.INFO)
            logging.error(self.error)
            return False
        return True

    def is_complete(self, instructions:dict):
        """
        instructions -> dict: dictionnary with all instructions
        verify that the dictionnary is complete 
        """
        for i in range(1, len(instructions) + 1):
            if len(instructions[str(i)]) != 3:
                self.error = f"Missing instructions line"
                logging.basicConfig(filename="latest.log", level=logging.INFO)
                logging.error(self.error)
                return False


    def start(self, ui, instructions:dict, current_value_label, next_value_label, background, tape_memory = Tape(), delay = 0):
        """Executes the program when called. Used instead of '__init__' so we can decide when to start it. The core of the program, which executes instructions as a Turing machine would do.

        Args:
            instructions (dict): Contains every instructions of the program loaded.
            tape_memory (class): The tape where data are written. Here it isn't optionnal but written as so for my text editor to understand what objects are used
            delay (int, optional): The delay used for the slowed down execution. Defaults to 0.
        """
        iterations = len(instructions)
        self.current_state = "1"
        while iterations > 0:
            tape_index = tape_memory.position
            tape_index_value = tape_memory.read(tape_index)

            sub_instruction = instructions[self.current_state][tape_index_value]

            current_value_label.config(text=tape_index_value)
            next_value_label.config(text=sub_instruction[0])

            if sub_instruction[0] == "-":
                tape_memory.write(ui, tape_index, tape_index_value)
            else :
                tape_memory.write(ui, tape_index, sub_instruction[0])

            if sub_instruction[1] != "-":
                tape_memory.move(ui, sub_instruction[1])

            if sub_instruction[2] == "f":
                iterations = 0
                top_level = tk.Toplevel(ui.root)
                ui.root.eval(f'tk::PlaceWindow {str(top_level)} center')
                tk.Label(top_level, text=i18n.t("done")).pack()
                tk.Button(top_level, text=i18n.t("quit"),command= top_level.destroy).pack()
            else:
                previous_state = self.current_state
                self.current_state = sub_instruction[2]
                if previous_state != self.current_state:
                    iterations -= 1

            ui.__dict__[f"label_state{self.current_state}"].config(bg=background)
            ui.__dict__[f"label_read{self.current_state}_{tape_index_value}"].config(bg=background)
            ui.__dict__[f"label_write{self.current_state}_{tape_index_value}"].config(bg=background)
            ui.__dict__[f"label_move{self.current_state}_{tape_index_value}"].config(bg=background)
            ui.__dict__[f"label_new_state{self.current_state}_{tape_index_value}"].config(bg=background)

            ui.canvas2.update()
            ui.circles.update()
            sleep(delay)
            for key in ui.__dict__.keys():
                if key.startswith("label"):
                    ui.__dict__[key].config(bg="grey94")