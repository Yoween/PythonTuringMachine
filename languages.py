import os, sys, i18n, json
import tkinter as tk

def initialisation(self):
    self.config_file = os.path.dirname(os.path.abspath(__file__)) + "\\config.json"
    if not os.path.exists(self.config_file):
        print(os.path.exists(self.config_file))
        with open(self.config_file, 'w') as fp:
            fp.write('{"language":"en"}')
    print(self.config_file)
    i18n.load_path.append(os.path.dirname(os.path.abspath(__file__)) + "\\translations")
    print(i18n.load_path)
    i18n.set("filename_format", "{locale}.{format}")
    with open(self.config_file, "r") as f:
        self.config = json.load(f)
    i18n.set("locale", self.config["language"])
    
def change_language(self, language):
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