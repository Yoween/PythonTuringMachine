# Python_Turing_Machine_NoGUI.py
#
# LAROCHE Tristan
# 30-01-2023
#==================================

import logging, time
import tkinter.filedialog as fd

class Tape() :
    def __init__(self) :
        self.tape = ["b"] * 10
        self.origin = 1
        self.position = 1
    
    def read(self, index: int) :
        return self.tape[index]
    
    def read_a(self) :
        x = str(self.tape[0])
        for element in self.tape[1:len(self.tape)] :
            x += ", " + str(element)
        return x
        
    def write(self, index: int, value: str, direction = 0) :
        if index >= len(self.tape) :
            self.tape.append(value)
        else :
            self.tape[index] = value

    def move(self, direction: str) :
        if direction == "<" :
            self.set_position(self.get_position()-1)
            if self.get_position() < 0 :
                self.tape = ["b"] + self.tape
                self.set_position(self.get_position() + 1)
                self.set_origin(self.get_origin()+1)
        if direction == ">" :
            self.set_position(self.get_position() + 1)
            if self.get_position() >= len(self.tape) :
                self.tape.append("b")

    def set_position(self, value: int) :
        self.position = value

    def get_position(self) :
        return self.position

    def set_origin(self, value: int):
        self.origin = value

    def get_origin(self) -> int:
        return self.origin


class ReadInstructions():
    allowed_characters = ("b", ">", "<", "f", "-")
    instructions = {}
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
            ExecuteInstructions(self.instructions)
        return (self.instructions) 

    def is_valid(self, characters:list, line:int):
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


class ExecuteInstructions():
    tape_memory = Tape()
    def __init__(self, instructions:dict):
        setup = 1
        while setup == 1:
            tape_index = self.tape_memory.get_position()
            print(f"Position: {tape_index}, Tape: {self.tape_memory.tape}")
            value = int(input("8 to move\n5 to write\n7 to quit setup\n1 to generate blank template\n0 to quit app\n"))
            if value == 8:
                direction = input("Direction to move (4|6): ")
                self.tape_memory.move("<" if direction == "4" else ">" if direction == "6" else "")
            elif value == 5:
                self.tape_memory.write(tape_index, input("Value to write (b|0|1): "))
            elif value == 7:
                break
            elif value == 1:
                self.generate_template()
            elif value == 0:
                exit()
        iterations = len(instructions)
        self.current_state = "1"
        while iterations > 0:
            tape_index = self.tape_memory.get_position()
            tape_index_value = self.tape_memory.read(tape_index)
                
            sub_insruction = instructions[self.current_state][tape_index_value]
            if sub_insruction[0] == "-":
                self.tape_memory.write(tape_index, tape_index_value)
            else :
                self.tape_memory.write(tape_index, sub_insruction[0])
                
            if sub_insruction[1] != "-":
                self.tape_memory.move(sub_insruction[1])
                
            if sub_insruction[2] == "f":
                iterations = 0
            else:
                previous_state = self.current_state
                self.current_state = sub_insruction[2]
                if previous_state != self.current_state:
                    iterations -= 1
        print(self.tape_memory.tape)
        input("Press any key to quit")

    def move(self, direction: str):
        self.tape_memory.move(direction)

    def write(self, value: str):
        self.tape_memory.write(value)

    def generate_template(self):
        steps = ("b", "0", "1")
        file = open(fd.askopenfilename(filetypes=[('Python Turing Machine (.ptm)', '*.ptm')]), "w")
        size = int(input("Enter the number of states you want: "))
        for i in range(1, int(size)+1):
            for j in range(3):
                file.write(f"{i} : {steps[j]} : - : - : {i}\n")
        file.close()

function_call = ReadInstructions()
returned_value = function_call.process(fd.askopenfilename(filetypes=[('Python Turing Machine (.ptm)', '*.ptm')]))