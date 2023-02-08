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
        self.tape = ["b"] * 29
        self.origin = 14
        self.position = 14

        
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
            while len(self.tape[:self.get_position()+1]) < 16 :
                self.tape = ["b"] + self.tape
                self.set_origin(self.get_origin()+1)
                self.set_position(self.get_position()+1)
            while len(self.tape[self.get_position():-1]) < 16 :
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
        
    def write(self, ui, index: int, value: str, direction = 0) :
        '''
            parameters :
        ui -> Class : the tkinter display
        index -> int : index of the value to change
        value -> str : new value of {self.tape} at index {index}
            return :
        return nothing, just change the value at index {index}
        '''
        if index >= len(self.tape) :
            self.tape.append(value)
        else :
            self.tape[index] = value
        for key in ui.circles.keys() :
                if self.tape[self.get_position() - int(key)] == 'b':
                    ui.circles[key][2] = 'white'
                if self.tape[self.get_position() - int(key)] == '0':
                    ui.circles[key][2] = 'blue'
                if self.tape[self.get_position() - int(key)] == '1':
                    ui.circles[key][2] = 'grey'
        ui.canvas2.destroy()
        ui.canvas2 = tk.Canvas(ui.right_tab, height=310,  bg='AntiqueWhite2')
        ui.canvas2.grid(row=2, column=0, columnspan=10, sticky='nesw')
        for value in ui.circles.values() :
            ui.drawcircle(ui.canvas2, value[0], value[1], 6, value[2])

    def move(self, ui, direction: str) :
        '''
            parameters :
            ui -> Class : the tkinter display
        direction -> str = '<' or '>' : the direction to forward in {self.tape}
            return :
        return nothing, just change call 'set_position()' to update the current position in {self.tape}
        '''
        if direction == "<" :
            self.set_position(self.get_position()+1)
            if len(self.tape[:self.get_position()+1]) < 16 :
                self.tape = ["b"] + self.tape
                self.set_position(self.get_position()-1)
                self.set_origin(self.get_origin()-1)

        if direction == ">" :
            self.set_position(self.get_position()-1)
            if len(self.tape[self.get_position():-1]) < 16 :
                self.tape.append("b")
                
        for key in ui.circles.keys() :
                if self.tape[self.get_position() - int(key)] == 'b':
                    ui.circles[key][2] = 'white'
                if self.tape[self.get_position() - int(key)] == '0':
                    ui.circles[key][2] = 'blue'
                if self.tape[self.get_position() - int(key)] == '1':
                    ui.circles[key][2] = 'grey'
        ui.canvas2.destroy()
        ui.canvas2 = tk.Canvas(ui.right_tab, height=310,  bg='AntiqueWhite2')
        ui.canvas2.grid(row=2, column=0, columnspan=10, sticky='nesw')
        for value in ui.circles.values() :
            ui.drawcircle(ui.canvas2, value[0], value[1], 6, value[2]) 

    def set_position(self, value: int) :
        '''
            parameters :
        value -> int : a number between -1 and 1
            return :
        retrun nothing, represent the movement towards the left or the right for the current position in {self.tape}
        '''
        self.position = value

    def get_position(self) :
        '''
            parameters :
        no parameters
            return :
        self.position -> int : curent position in {self.tape}
        '''
        return self.position

    def set_origin(self, value: int):
        '''
            parameters :
        no parameters
            return :
        return nothing, just update the origin, the index 0 at the creation of {the self.tape}
        '''
        self.origin = value

    def get_origin(self) -> int:
        '''
            parameters :
        no parameters 
            return :
        self.origin -> int : the original index 0 of {self.tape}
        '''
        return self.origin
        