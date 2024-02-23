"""
From Genius_um. Under the name of MazeGroup (https://mazegroup.org/)
2024
"""

import sys
import shutil
import os
import random as rd
import time
import subprocess
args = sys.argv
args = args[1:]

if not len(args):
    print("Usage : tang <path : folder to make package / .tpk to run package> <options>")
    sys.exit(1)

script_path = os.path.dirname(os.path.abspath(__file__))
temp_path = os.path.join(script_path, "temp")

if not os.path.exists(temp_path):
    os.mkdir(temp_path)

options = args[1:]

path = args[0]

class MKPKG():
    def __init__(self, path:str):
        self.path = path
        self.path = self.path.replace("\\", "/")
        shutil.make_archive(self.path.split("/")[-1], 'zip', self.path)
        try:
            os.rename(self.path.split("/")[-1] + ".zip", self.path.split("/")[-1] + ".tpk")
        except:
            os.remove(self.path.split("/")[-1] + ".tpk")
            os.rename(self.path.split("/")[-1] + ".zip", self.path.split("/")[-1] + ".tpk")

class RNPKG():
    def __init__(self, path:str):
        self.path = path
        self.temp_id = str(rd.randint(1000000000, 9999999999))
        self.temp_path = os.path.join(temp_path, self.temp_id)
        self.path = self.path.replace("\\", "/")
        shutil.unpack_archive(self.path, self.temp_path, "zip")
        self.essentials_items = ["entry.tip", "exit.tip", "info.tip", "package/", "package/__init__.py"]
        for essential_item in self.essentials_items:
            if not os.path.exists(os.path.join(self.temp_path, essential_item)):
                print(f"Essential item {essential_item} not found in package.")
                sys.exit(1)
        self.pkg_paths = {
            "entry": os.path.join(self.temp_path, "entry.tip"),
            "exit": os.path.join(self.temp_path, "exit.tip"),
            "info": os.path.join(self.temp_path, "info.tip"),
            "py_pkg": os.path.join(self.temp_path, "package/"),
            "init": os.path.join(self.temp_path, "package/__init__.py")
        }
        try:
            self.pkg_tip_contents = {
                "entry": dict(eval(open(self.pkg_paths["entry"], encoding="utf-8").read())),
                "exit": dict(eval(open(self.pkg_paths["exit"], encoding="utf-8").read())),
                "info": dict(eval(open(self.pkg_paths["info"], encoding="utf-8").read()))
            }
        except:
            print(f"Error during reading .tip files.")
            sys.exit(1)
        self.info_tip_ess = ["name", "author", "version", "desc"]
        for ess_item in self.info_tip_ess:
            if not ess_item in self.pkg_tip_contents["info"].keys():
                print(f"Not property '{ess_item}' found on info.tip.")
                sys.exit(1)

        self.entry_tip_ess = ["start", "init", "log", "clear"]
        for ess_item in self.entry_tip_ess:
            if not ess_item in self.pkg_tip_contents["entry"].keys():
                print(f"Not property '{ess_item}' found on entry.tip.")
                sys.exit(1)

        self.exit_tip_ess = ["finish", "log"]
        for ess_item in self.exit_tip_ess:
            if not ess_item in self.pkg_tip_contents["exit"].keys():
                print(f"Not property '{ess_item}' found on exit.tip.")
                sys.exit(1)

        if str(self.pkg_tip_contents["entry"]["start"]).strip() != "":
            self.entry_start_path = str(self.pkg_tip_contents["entry"]["start"]).strip()
        else:
            self.entry_start_path = False

        self.entry_init = bool(self.pkg_tip_contents["entry"]["init"])
        self.entry_log = bool(self.pkg_tip_contents["entry"]["log"])
        self.entry_clear = bool(self.pkg_tip_contents["entry"]["clear"])

        if str(self.pkg_tip_contents["exit"]["finish"]).strip() != "":
            self.exit_path = str(self.pkg_tip_contents["exit"]["finish"]).strip()
        else:
            self.exit_path = False

        self.exit_log = bool(self.pkg_tip_contents["exit"]["log"])

        self.info_name = str(self.pkg_tip_contents["info"]["name"]).strip()
        self.info_author = str(self.pkg_tip_contents["info"]["author"]).strip()
        self.info_version = str(self.pkg_tip_contents["info"]["version"]).strip().lower()
        self.info_desc = str(self.pkg_tip_contents["info"]["desc"]).strip()

        self.start_time = time.time()
        if self.entry_clear:
            os.system("cls")
        if self.entry_log:
            print(f"Executing package '{self.info_name}' {self.info_version} from {self.info_author}.\n")
        if self.entry_init:
            os.system(f"python \"{self.pkg_paths["init"]}\"")
        if self.entry_start_path != False:
            subprocess.run(f"python \"{os.path.join(self.temp_path, self.entry_start_path)}\"")
        if self.exit_path != False:
            subprocess.run(f"python \"{os.path.join(self.temp_path, self.exit_path)}\"")
        if self.exit_log:
            print(f"Package execution finished in {round(time.time() - self.start_time, 4)}s.")

if os.path.exists(path):
    if os.path.isdir(path):
        if "-r" in options:
            MKPKG(path)
            RNPKG(path + ".tpk")
        else:
            MKPKG(path)
    else:
        RNPKG(path)
else:
    print("Path not exists.")
    sys.exit(1)