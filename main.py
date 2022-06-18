from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

ttk.Label(frame, text="test text").grid(column=0, row=0)
ttk.Label(frame, text="By Tomiwa Shobowale and Oghenetega Gbejewoh").grid(column=0, row=1);

root.mainloop()
