# Tape.py
#
# ADAM Loris
# ??-??-????
#==================================

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
        
    def write(self, index: int, value: str, direction = 0) :
        '''
            parameters : 
        index -> int : index of the value to change
        value -> str : new value of {self.tape} at index {index}
            return :
        return nothing, just change the value at index {index}
        '''
        if index >= len(self.tape) :
            self.tape.append(value)
        else :
            self.tape[index] = value

    def move(self, direction: str) :
        '''
            parameters :
        direction -> str = '<' or '>' : the direction to forward in {self.tape}
            return :
        return nothing, just change call 'set_position()' to update the current position in {self.tape}
        '''
        if direction == "<" :
            self.set_position(self.get_position()-1)
            while len(self.tape[:self.get_position()+1]) < 16 :
                self.tape = ["b"] + self.tape
                self.set_origin(self.get_origin()+1)

        if direction == ">" :
            self.set_position(self.get_position()+1)
            while len(self.tape[self.get_position():-1]) < 16 :
                self.tape.append("b")

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
        