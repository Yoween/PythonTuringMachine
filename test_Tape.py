#!/usr/bin/env python3
from Tape import Tape

def test___init__():
    ui = False
    a = Tape()
    assert a.tape == ["b"] * 51
    assert a.position == 25
    assert a.origin == 25

def test_read():
    a = Tape()
    ui = False
    assert a.read(29) == 'b'
    a.write(ui, 18, '1')
    assert a.read(18) == '1'

def test_read_all():
    a = Tape()
    ui = False
    assert a.read_all() == "b, " * 50 + "b"
    for index in range(len(a.tape)) :
        a.write(ui, index, '1')
    assert a.read_all() == "1, " * 50 + "1"

def test_move():
    ui = False
    a= Tape()
    a.move(ui, '>')
    assert a.tape == ["b"] * 51
    assert a.position == 26
    assert a.position == 26
    
def test_write():
    ui = False
    a = Tape()
    a.write(ui, a.position,'1')
    assert a.tape == ["b"]*25 + ["1"] + ["b"]*25