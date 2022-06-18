from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frame, text="Cookie Game").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Label(frame, text="By Oluwatomiwa Shobowale and Oghenetega Gbejewoh").grid(column=0, row=1);

root.mainloop()
