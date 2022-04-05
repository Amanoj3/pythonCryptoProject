"""
note to self:
- modify scene by moving buttons
- create methods for buttons
- create a text-area of some sort
- create unit test cases
- create another scene/stage that displays a graph of some sort
"""

#the driver file

from tkinter import *
from Application import Application
root = Tk()
root.geometry('350x100')
root.title("Not an earth-shattering project")
app = Application(master=root)
app.mainloop()