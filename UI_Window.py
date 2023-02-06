# ui_choice1.py
# 
# ADAM Loris, LAROCHE Tristan
# 20-Dec-2022
#==================================

import tkinter as tk
import os, sys, i18n, json
from Tape import Tape
from execute_code import import_code, execute_code, move, write, clear_tape
from generate_template import generate_template, help
from scrollable_frame import scroll_bar
from languages import initialisation, change_language


class UI_Window():
    """This is the class where everything in the program takes place.
    """
    def __init__(self):
        """This is the main window; it displays every element of the user interface when the program starts.
        """
        initialisation(self)
        
        
        self.width = 720
        self.height = 480
        self.root = tk.Tk()
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, int(self.root.winfo_screenwidth()/2 - self.width/2),
                                        int(self.root.winfo_screenheight()/2 - self.height/2)))
        self.root.resizable(width=False, height=False)

        self.root.title(i18n.t("main_title"))
        self.root.bind("<Control-o>", lambda y: import_code(self))
        self.instructions = {}
        self.execution = ()
        self.tape_memory = Tape()
        self.default_path = os.path.abspath(__file__) + "/../default_templates"

        self.menu = tk.Menu(self.root)    
        self.menu_file = tk.Menu(tearoff=0)
        self.menu.add_cascade(label=i18n.t("file"), menu=self.menu_file)
        self.menu_file.add_command(label=i18n.t("open"), command= lambda: import_code(self))
        self.menu_file.add_command(label=i18n.t("exit"), command=lambda: self.root.destroy())

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
        
        self.menu.add_command(label=i18n.t("help"), command= lambda: help(self))

        self.root.config(menu=self.menu)        


        # Left part

        self.code_tab = tk.Frame(self.root)

        scroll_bar(self, self.code_tab, self.root.winfo_screenwidth(), self.root.winfo_screenheight())

        text_name = ("state", "read", "write", "move", "new_state")

        for i in range(5) :

            self.__dict__[f"label_{text_name[i]}"] = tk.Label(self.scrollable_frame, text=f"{i18n.t(text_name[i])}", relief=tk.RIDGE)
            self.__dict__[f"label_{text_name[i]}"].grid(row=0, column=i, sticky='nesw')



        self.code_tab.pack(side='left', expand=True, fill='both')
        self.canvas.pack(side="left", fill="both", expand=True, ipadx=60)
        self.scrollbar.pack(side="right", fill="y")
        for i in range(5) :
            self.scrollable_frame.columnconfigure(i, weight=1)

        

        # Right part

        self.turing_tab = tk.Frame(self.root, bg='AntiqueWhite2')

        self.canvas2 = tk.Canvas(self.turing_tab, height=310)
        self.canvas2.grid(row=2, column=0, columnspan=10, sticky='nesw')

        self.button_go = tk.Button(self.turing_tab, text=i18n.t("start"), command= lambda: execute_code(self, self.instructions, slow_execution_var.get()))
        self.button_go.grid(row=10, column=1, sticky='nesw')
        self.button_left = tk.Button(self.turing_tab, text=i18n.t("left"), command= lambda: move(self, "<"))
        self.button_left.grid(row=10, column=2, sticky='nesw')
        self.button_right = tk.Button(self.turing_tab, text=i18n.t("right"), command= lambda: move(self, ">"))
        self.button_right.grid(row=10, column=3, sticky='nesw')
        self.button_clear = tk.Button(self.turing_tab, text=i18n.t("clear"), command= lambda: clear_tape(self))
        self.button_clear.grid(row=10, column=4, sticky='nesw')
        
        slow_execution_var = tk.IntVar()
        self.button_slow = tk.Checkbutton(self.turing_tab, text=i18n.t("slow"), variable= slow_execution_var, offvalue= 0, onvalue= 1)
        self.button_slow.grid(row=11, column=1, sticky='nesw')
        self.button_b = tk.Button(self.turing_tab, text="b", command= lambda: write(self, "b"))
        self.button_b.grid(row=11, column=2, sticky='nesw')
        self.button_0 = tk.Button(self.turing_tab, text="0", command= lambda: write(self, "0"))
        self.button_0.grid(row=11, column=3, sticky='nesw')
        self.button_1 = tk.Button(self.turing_tab, text="1", command= lambda: write(self, "1"))
        self.button_1.grid(row=11, column=4, sticky='nesw')

        self.drawcircle(self.canvas2, 40, 20, 6, 'red')
        self.drawcircle(self.canvas2, 42, 40, 6, 'red')
        self.drawcircle(self.canvas2, 45, 60, 6, 'red')
        self.drawcircle(self.canvas2, 49, 80, 6, 'red')
        self.drawcircle(self.canvas2, 54, 100, 6, 'red')
        self.drawcircle(self.canvas2, 60, 120, 6, 'red')
        self.drawcircle(self.canvas2, 68, 140, 6, 'red')
        self.drawcircle(self.canvas2, 78, 160, 6, 'red')
        self.drawcircle(self.canvas2, 90, 180, 6, 'red')
        self.drawcircle(self.canvas2, 104, 200, 6, 'red')
        self.drawcircle(self.canvas2, 120, 220, 6, 'red')
        self.drawcircle(self.canvas2, 138, 240, 6, 'red')
        self.drawcircle(self.canvas2, 158, 260, 6, 'red')
        self.drawcircle(self.canvas2, 180, 270, 6, 'red')
        self.drawcircle(self.canvas2, 204, 275, 6, 'red')
        self.drawcircle(self.canvas2, 228, 270, 6, 'red')
        self.drawcircle(self.canvas2, 250, 260, 6, 'red')
        self.drawcircle(self.canvas2, 270, 240, 6, 'red')
        self.drawcircle(self.canvas2, 288, 220, 6, 'red')
        self.drawcircle(self.canvas2, 304, 200, 6, 'red')
        self.drawcircle(self.canvas2, 318, 180, 6, 'red')
        self.drawcircle(self.canvas2, 330, 160, 6, 'red')
        self.drawcircle(self.canvas2, 340, 140, 6, 'red')
        self.drawcircle(self.canvas2, 348, 120, 6, 'red')
        self.drawcircle(self.canvas2, 354, 100, 6, 'red')
        self.drawcircle(self.canvas2, 359, 80, 6, 'red')
        self.drawcircle(self.canvas2, 363, 60, 6, 'red')
        self.drawcircle(self.canvas2, 366, 40, 6, 'red')
        self.drawcircle(self.canvas2, 368, 20, 6, 'red')

        self.turing_tab.pack(side='right', expand=True, fill='both')

        print(self.canvas2['height'])
        print(self.canvas2['width'])
        
        
    def creation(self):
        """This function is invoked when loading a file to clear the previous instructions and display the new ones.
        """
        self.code_tab.destroy()
        self.code_tab = tk.Frame(self.root)

        scroll_bar(self, self.code_tab, self.root.winfo_screenwidth(), self.root.winfo_screenheight())

        text_name = ("state", "read", "write", "move", "new_state")

        for i in range(5) :

            self.__dict__[f"label_{text_name[i]}"] = tk.Label(self.scrollable_frame, text=f"{i18n.t(text_name[i])}", relief=tk.RIDGE)
            self.__dict__[f"label_{text_name[i]}"].grid(row=0, column=i, sticky='nesw')

        self.code_tab.pack(side='left', expand=True, fill='both')
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        for i in range(5) :
            self.scrollable_frame.columnconfigure(i, weight=1)

        x = 1
        while f"label_state{x}" in self.__dict__.keys() :
            del self.__dict__[f"label_state{x}"]

            del self.__dict__[f"label_state{x}_b"]
            del self.__dict__[f"label_state{x}_0"]
            del self.__dict__[f"label_state{x}_1"]

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
                for i in range(3) :
                    self.__dict__[f"label_state{x}"] = tk.Label(self.scrollable_frame, text= f"{x}")
                    self.__dict__[f"label_state{x}"].grid(row=3*x-2, rowspan= 3, column=0, sticky='nesw')

                    self.__dict__[f"label_state{x}_{key[i]}"] = tk.Label(self.scrollable_frame, text= f"{key[i]}")
                    self.__dict__[f"label_state{x}_{key[i]}"].grid(row=3*x-2+i, column=1, sticky='nesw')

                    self.__dict__[f"label_write{x}_{key[i]}"] = tk.Label(self.scrollable_frame, text= f"{instructions[key[i]][0]}")
                    self.__dict__[f"label_write{x}_{key[i]}"].grid(row=3*x-2+i, column= 2, sticky='nesw')

                    self.__dict__[f"label_move{x}_{key[i]}"] = tk.Label(self.scrollable_frame, text= f"{instructions[key[i]][1]}")
                    self.__dict__[f"label_move{x}_{key[i]}"].grid(row=3*x-2+i, column= 3, sticky='nesw')

                    self.__dict__[f"label_new_state{x}_{key[i]}"] = tk.Label(self.scrollable_frame, relief=tk.RIDGE ,text=f'{instructions[key[i]][2]}')
                    self.__dict__[f"label_new_state{x}_{key[i]}"].grid(row=3*x-2+i, column=4, sticky='nesw')
                amount -= 1
            x += 1

    def drawcircle(self, canv, x, y, rad, color):
        canv.create_oval(x-rad, y-rad, x+rad, y+rad, width=0, fill=f'{color}')

if __name__ ==  '__main__' :
    a = UI_Window()
    a.root.mainloop()

a = 0
