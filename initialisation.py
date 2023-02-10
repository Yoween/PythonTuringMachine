#!/usr/bin/env python3
# languages.py
#
# LAROCHE Tristan
# 06-02-2023
#==================================

import os, sys, i18n, json
import tkinter as tk

def initialisation(self):
    """
    initialisation of everything
    """
    self.config_file = os.getcwd() + "/config.json"
    if not os.path.exists(self.config_file):
        with open(self.config_file, 'w') as fp:
            fp.write('{"language": "fr", "highlight_color": "lightblue", "one_color": "blue", "zero_color": "grey"}')
    i18n.load_path.append(os.getcwd() + "/translations")
    i18n.set("filename_format", "{locale}.{format}")
    with open(self.config_file, "r") as f:
        self.config = json.load(f)
    i18n.set("locale", self.config["language"])
    self.background_color = self.config["highlight_color"]
    self.one_color = self.config["one_color"]
    self.zero_color = self.config["zero_color"]

def change_language(self, language):
    """
    permute between english and french
    """
    with open(self.config_file, "w") as f:
        self.config["language"] = language
        json.dump(self.config, f)
    self.restart_window = tk.Toplevel(self.root)
    self.restart_window.attributes('-topmost', 'true')
    self.restart_window.geometry('%dx%d+%d+%d' % (400, 80, int(self.root.winfo_screenwidth()/2 - 400/2),
                                    int(self.root.winfo_screenheight()/2 - 80/2)))
    tk.Label(self.restart_window, text=i18n.t("restart_required")).pack()
    tk.Button(self.restart_window, text=i18n.t("indeed"), command= lambda: os.execv(sys.executable, ['python'] + sys.argv)).pack()
    tk.Button(self.restart_window, text=i18n.t("please_no"), command= self.restart_window.destroy).pack()