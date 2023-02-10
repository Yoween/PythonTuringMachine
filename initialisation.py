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
            fp.write('{"language": "en", "color_highlight": "lightblue", "color_blank": "white", "color_zero": "dark sea green", "color_one": "coral"}')
    i18n.load_path.append(os.getcwd() + "/translations")
    i18n.set("filename_format", "{locale}.{format}")
    with open(self.config_file, "r") as f:
        self.config = json.load(f)
    i18n.set("locale", self.config["language"])
    self.color_highlight = self.config["color_highlight"]
    self.color_blank = self.config["color_blank"]
    self.color_zero = self.config["color_zero"]
    self.color_one = self.config["color_one"]