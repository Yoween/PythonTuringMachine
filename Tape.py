#!/usr/bin/env python3
# Tape.py
#
# ADAM Loris
# ??-??-????
#==================================
import tkinter as tk
class Tape() :
    def __init__(self) :
        '''
            parameters : 
        no parameters 
            return :
        return nothing, just create the list {self.tape}, the {self.origin} who is the index 0 of {self.tape}
                        and {self.position} the current position in the tape
        '''
        self.tape = ["b"] * 51
        self.origin = 25
        self.position = 25

        
    def read(self, index: int) :
        '''
            parameters : 
        index -> int : index of the value to return
            return :
        self.tape[index] -> str : return the value of the list at index {index}
        '''
        try :
            return self.tape[index]
        except :
            while len(self.tape[:self.position+1]) < 16 :
                self.tape = ["b"] + self.tape
                self.origin += 1
                self.position += 1
            while len(self.tape[self.position:-1]) < 16 :
                self.tape.append("b")
    
    def read_all(self) :
        '''
            parameters : 
        no parameters
            return :
        x -> str : a string contain all values of {self.tape}
        '''
        x = str(self.tape[0])
        for element in self.tape[1:len(self.tape)] :
            x += ", " + str(element)
        return x
        
    def write(self, ui, index: int, value: str) :
        """Writes the provided value in the provided cell at provided index

        Args:
            ui (class): Called to update the display
            index (int): The position you're at
            value (str): The value you write at the position
        """
        if index >= len(self.tape) :
            self.tape.append(value)
        else :
            self.tape[index] = value
            
        self.update_display(ui)

    def move(self, ui, direction: str) :
        """Move on the tape in the provided directions

        Args:
            ui (class): Called to update the display
            direction (str): The direction you move (">" or "<")
        """
        if direction == "<" :
            self.position -= 1
            if len(self.tape[:self.position+1]) < 16 :
                self.tape = ["b"] + self.tape
                self.position += 1
                self.origin -= 1

        if direction == ">" :
            self.position += 1
            if len(self.tape[self.position:-1]) < 16 :
                self.tape.append("b")
                
        self.update_display(ui)

    def update_display(self, ui):
        for key in ui.circles.keys() :
            if self.tape[self.position - int(key)] == 'b':
                ui.circles[key][2] = 'white'
            if self.tape[self.position - int(key)] == '0':
                ui.circles[key][2] = 'grey'
            if self.tape[self.position - int(key)] == '1':
                ui.circles[key][2] = 'blue'
        ui.canvas2.destroy()
        ui.canvas2 = tk.Canvas(ui.right_tab, height=310,  bg='AntiqueWhite2')
        ui.canvas2.grid(row=2, column=0, columnspan=10, sticky='nesw')
        for value in ui.circles.values() :
            ui.drawcircle(ui.canvas2, value[0], value[1], 6, value[2]) 