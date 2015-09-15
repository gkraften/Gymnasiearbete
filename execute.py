import tkinter.simpledialog as dialog
from tkinter import Tk
from subprocess import call
import sys


root = Tk()
root.lift()
if sys.platform == "darwin":
    call(["osascript", "-e", 'tell app "Finder" to set frontmost of process "Robot" to true'])
root.withdraw()
print(dialog.askstring("Titel", "Undertitel"))