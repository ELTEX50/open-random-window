from tkinter import *
import random

for i in range(0, 1000, 100):
    root = Tk()
    root.geometry(f'{random.randint(50,400)}x{random.randint(50,400)}'
    f'+{random.randint(0, 800)}+{random.randint(0, 800)}')


root.mainloop()