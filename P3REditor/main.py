import os, sys

from P3REditor.p3rsaveold import P3RSave
from P3REditor.prompt import Prompt
from P3REditor.savemanager import SaveManager


def process_save_file():
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("Type the Persona3 file name (must be located in this folder) :")
    if os.path.exists(target):
        save_manager = SaveManager()
        p3rsave = save_manager.load(target)
        prompt = Prompt(p3rsave, save_manager)
        prompt.run()



    else:
        raise FileNotFoundError("File not found")
