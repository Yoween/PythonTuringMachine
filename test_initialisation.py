#!/usr/bin/env python3

import os, json

def test_initialisation():
    config_file = os.getcwd() + "/config.json"
    with open(config_file, "r") as f:
        config = json.load(f)
    for i in ["language", "color_highlight", "color_blank", "color_zero", "color_one"]:
        assert i in config.keys() #checks if every key exists