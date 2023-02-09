#!/usr/bin/env python3
# UI_Window.py
# 
# ADAM Loris, LAROCHE Tristan
# 20-Dec-2022
#==================================

import tkinter as tk
import os, i18n, webbrowser, subprocess
from Tape import Tape
from execute_code import import_code, execute_code, move, write, clear_tape
from generate_template import generate_template
from initialisation import initialisation, change_language


class UI_Window():
    """This is the class where everything in the program takes place.
    """
    def __init__(self):
        """This is the main window; it displays every element of the user interface when the program starts.
        """
        initialisation(self)
        
        
        self.width = 1080
        self.height = 720
        self.root = tk.Tk()
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, int(self.root.winfo_screenwidth()/2 - self.width/2),
                                        int(self.root.winfo_screenheight()/2 - self.height/2)))
        self.root.resizable(width=False, height=False)

        self.root.title(i18n.t("main_title"))
        self.root.bind("<Control-o>", lambda y: import_code(self))
        self.instructions = {}
        self.execution = ()
        self.circles = {'14': [40, 20, 'white'], '13': [42, 40, 'white'], '12': [45, 60, 'white'], '11': [49, 80, 'white'], '10': [54, 100, 'white'],
                        '9': [60, 120, 'white'], '8': [68, 140, 'white'], '7': [78, 160, 'white'], '6': [90, 180, 'white'], '5': [104, 200, 'white'],
                        '4': [118, 220, 'white'], '3': [136, 237, 'white'], '2': [156, 252, 'white'], '1': [178, 265, 'white'], '0': [204, 270, 'white'],
                        '-1': [228, 265, 'white'], '-2': [250, 252, 'white'], '-3': [270, 237, 'white'], '-4':[288, 220, 'white'], '-5': [304, 200, 'white'],
                        '-6': [318, 180, 'white'], '-7': [330, 160, 'white'], '-8': [340, 140, 'white'], '-9': [348, 120, 'white'], '-10': [354, 100, 'white'],
                        '-11': [359, 80, 'white'], '-12': [363, 60, 'white'], '-13': [366, 40, 'white'], '-14': [368, 20, 'white']}
        self.tape_memory = Tape()
        self.default_path = os.getcwd() + "/default_templates"

        self.menu = tk.Menu(self.root)    
        self.menu_file = tk.Menu(tearoff=0)
        self.menu.add_cascade(label=i18n.t("file"), menu=self.menu_file)
        self.menu_file.add_command(label=i18n.t("open"), command= lambda: import_code(self))
        self.menu_file.add_command(label=i18n.t("exit"), command=self.root.destroy)

        self.menu_templates = tk.Menu(tearoff=0)
        self.menu.add_cascade(label=i18n.t("templates"), menu=self.menu_templates)
        self.menu_templates.add_command(label=i18n.t("generate"), command= lambda: generate_template(self))
        self.menu_load_template = tk.Menu(tearoff=0)
        self.menu_templates.add_cascade(label=i18n.t("load"), menu=self.menu_load_template)
        self.menu_load_template.add_command(label=i18n.t("invert_value"), command= lambda: import_code(self, f"{self.default_path}/invert_values.ptm"))
        self.menu_load_template.add_command(label=i18n.t("add_one"), command= lambda: import_code(self, f"{self.default_path}/add_one_binary.ptm"))
        self.menu_load_template.add_command(label=i18n.t("remove_one"), command= lambda: import_code(self, f"{self.default_path}/remove_one_binary.ptm"))
        
        self.menu_languages = tk.Menu(tearoff=0)
        self.menu.add_cascade(label=i18n.t("language"), menu=self.menu_languages)
        self.menu_languages.add_command(label="English", command=lambda: change_language(self, "en"))
        self.menu_languages.add_command(label="Français", command=lambda: change_language(self, "fr"))
        
        self.menu.add_command(label=i18n.t("help"), command= lambda: subprocess.Popen([os.getcwd() + "/machinedeturingenpython.pdf"], shell = True) )
        
        self.menu.add_command(label="Github", command= lambda: webbrowser.open("https://github.com/Yoween/PythonTuringMachine"))

        self.root.config(menu=self.menu)        

        self.execution_tab()
        self.preview_tab()


    def execution_tab(self):
        """
        Create the display for the execution, each bloc of lines is a different row on the display
        """
        try:
            self.right_tab.destroy()
        except:
            pass
        self.right_tab = tk.Frame(self.root, bg='AntiqueWhite2')

        self.canvas2 = tk.Canvas(self.right_tab, height=310,  bg='AntiqueWhite2')
        self.canvas2.grid(row=1, column=0, columnspan=8, sticky='nesw')
        for value in self.circles.values() :
            self.drawcircle(self.canvas2, value[0], value[1], 6, value[2])

        self.button_go = tk.Button(self.right_tab, text=i18n.t("start"), command= lambda: execute_code(self, self, self.instructions, slow_execution_var.get()))
        self.button_go.grid(row=10, column=1, sticky='nesw')
        self.button_clear = tk.Button(self.right_tab, text=i18n.t("clear"), command= lambda: clear_tape(self, self))
        self.button_clear.grid(row=10, column=2, sticky='nesw')
        self.button_left = tk.Button(self.right_tab, text=i18n.t("left"), command= lambda: move(self, self, "<"))
        self.button_left.grid(row=10, column=3, sticky='nesw')
        self.button_right = tk.Button(self.right_tab, text=i18n.t("right"), command= lambda: move(self, self, ">"))
        self.button_right.grid(row=10, column=4, sticky='nesw')
        self.current_label = tk.Label(self.right_tab, text=i18n.t("value"))
        self.current_label.grid(row=10, column=5)
        self.next_label = tk.Label(self.right_tab, text=i18n.t("next_value"))
        self.next_label.grid(row=10, column=6)
        
        slow_execution_var = tk.IntVar()
        self.button_slow = tk.Checkbutton(self.right_tab, text=i18n.t("slow"), variable= slow_execution_var, offvalue= 0, onvalue= 1)
        self.button_slow.grid(row=11, column=1, sticky='nesw')
        self.button_b = tk.Button(self.right_tab, text="b", command= lambda: write(self, self, "b"))
        self.button_b.grid(row=11, column=2, sticky='nesw')
        self.button_0 = tk.Button(self.right_tab, text="0", command= lambda: write(self, self, "0"))
        self.button_0.grid(row=11, column=3, sticky='nesw')
        self.button_1 = tk.Button(self.right_tab, text="1", command= lambda: write(self, self, "1"))
        self.button_1.grid(row=11, column=4, sticky='nesw') 
        self.current_value = tk.Label(self.right_tab, text="")
        self.current_value.grid(row=11, column=5)
        self.next_value = tk.Label(self.right_tab, text="")
        self.next_value.grid(row=11, column=6)

        self.right_tab.pack(side='right', expand=True, fill='both')
        for i in range(5) :
            self.right_tab.columnconfigure(i, weight=1)
        
    def preview_tab(self):
        """This function is invoked when loading a file to clear the previous instructions and display the new ones.
        """
        try:
            self.left_tab.destroy() 
        except:
            pass
        self.left_tab = tk.Frame(self.root)

        self.scroll_bar(self, self.left_tab, self.root.winfo_screenwidth())

        self.text_name = ("state", "read", "write", "move", "new_state")
        for i in range(5) :

            self.__dict__[f"label_{self.text_name[i]}"] = tk.Label(self.scrollable_frame, text=f"{i18n.t(self.text_name[i])}", relief=tk.RIDGE) 
            self.__dict__[f"label_{self.text_name[i]}"].grid(row=0, column=i, sticky='nesw')

        self.left_tab.pack(side='left', expand=True, fill='both')
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        for i in range(5) :
            self.scrollable_frame.columnconfigure(i, weight=1)

        x = 1
        while f"label_state{x}" in self.__dict__.keys() :
            # Delete all function which serve for the display of the code
            del self.__dict__[f"label_state{x}"]

            del self.__dict__[f"label_read{x}_b"]
            del self.__dict__[f"label_read{x}_0"]
            del self.__dict__[f"label_read{x}_1"]

            del self.__dict__[f"label_write{x}_b"] 
            del self.__dict__[f"label_write{x}_0"] 
            del self.__dict__[f"label_write{x}_1"] 

            del self.__dict__[f"label_move{x}_b"]
            del self.__dict__[f"label_move{x}_0"]
            del self.__dict__[f"label_move{x}_1"]

            del self.__dict__[f"label_new_state{x}_b"]
            del self.__dict__[f"label_new_state{x}_0"]
            del self.__dict__[f"label_new_state{x}_1"]
            x += 1

        self.scrollable_frame.update()


    def new_state(self, instructions: dict):
        """Displays new instructions after previous ones got cleared

        Args:
            instructions (dict): Contains every instructions of the program loaded.
        """
        amount = 1
        x = 1
        key = ("b","0","1")
        while amount > 0:
            if not f'label_state{x}' in self.__dict__.keys() :
                # test if the variable already exists 
                for i in range(3) :
                    # Create each line for the State in code display
                    self.__dict__[f"label_state{x}"] = tk.Label(self.scrollable_frame, text= f"{x}")
                    self.__dict__[f"label_state{x}"].grid(row=3*x-1, column=0, sticky='nesw')
                    tk.Label(self.scrollable_frame, text= '||').grid(row=3*x, column=0, sticky='nesw')
                    tk.Label(self.scrollable_frame, text= '||').grid(row=3*x-2, column=0, sticky='nesw')

                    self.__dict__[f"label_read{x}_{key[i]}"] = tk.Label(self.scrollable_frame, text= f"{key[i]}")
                    self.__dict__[f"label_read{x}_{key[i]}"].grid(row=3*x-2+i, column=1, sticky='nesw')

                    self.__dict__[f"label_write{x}_{key[i]}"] = tk.Label(self.scrollable_frame, text= f"{instructions[key[i]][0]}")
                    self.__dict__[f"label_write{x}_{key[i]}"].grid(row=3*x-2+i, column= 2, sticky='nesw')

                    self.__dict__[f"label_move{x}_{key[i]}"] = tk.Label(self.scrollable_frame, text= f"{instructions[key[i]][1]}")
                    self.__dict__[f"label_move{x}_{key[i]}"].grid(row=3*x-2+i, column= 3, sticky='nesw')

                    self.__dict__[f"label_new_state{x}_{key[i]}"] = tk.Label(self.scrollable_frame, text=f'{instructions[key[i]][2]}')
                    self.__dict__[f"label_new_state{x}_{key[i]}"].grid(row=3*x-2+i, column=4, sticky='nesw')

                amount -= 1
            x += 1

    def drawcircle(self, canv: object, x: int, y:int , rad:int, color:str):
        """
        canv -> class : the canvas to draw in 
        x -> int : position in abscissa for the circle
        y -> int : position in ordinate for the circle
        rad -> int : radius of the circle
        color -> str : the color of the circles 
        create the circles with the color for the state, blank 'b', gray '0', blue '1'
        """
        canv.create_oval(x-rad, y-rad, x+rad, y+rad, width=0, fill=f'{color}')
        
    def scroll_bar(self, container: object, width: int) :
        """
        container -> class: the that will contains the scroll bar
        width -> int: the width of the left tab in pixels 
        create the canvas and the scrollable frame and the scroll bar
        """
        self.canvas = tk.Canvas(container, width=int(width/9), bg='gray94')
        self.scrollbar = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=int(width/6))
        self.canvas.configure(yscrollcommand=self.scrollbar.set)


if __name__ ==  '__main__' :
    # Start the programm
    a = UI_Window()
    a.root.mainloop()