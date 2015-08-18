#!/usr/bin/env python

import yaml
import os
from colorama import Fore
import subprocess
def registerProjects(workspace):
    print Fore.CYAN + "Registering workspace:", workspace + Fore.RESET
    src_dir = os.path.join(workspace, "..", "src")
    rosinstall_path = os.path.join(src_dir, ".rosinstall")
    if os.path.exists(rosinstall_path):
        with open(rosinstall_path, "r") as f:
            for data in yaml.load(f):
                if data.has_key("git") and data["git"].has_key("local-name"):
                    project_dir = os.path.join(src_dir, data["git"]["local-name"])
                    print Fore.RED + "Project found:", project_dir, Fore.RESET
                    subprocess.check_call(["milk", "add", os.path.abspath(project_dir)])

if __name__ == "__main__":
    paths = os.environ["CMAKE_PREFIX_PATH"]
    for workspace in paths.split(":"):
        registerProjects(workspace)
