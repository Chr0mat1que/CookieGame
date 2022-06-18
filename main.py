from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("800x600")
frame = ttk.Frame(root)
frame.grid()

desc = ttk.Label(frame, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", wraplength=800, justify="center") # This is the description text, stating what the game is about and other important information.
desc.grid(column=0, columnspan=2, row=0)

start_btn = ttk.Button(frame, text="Start").grid(column=0, row=1)
exit_btn = ttk.Button(frame, text="Exit").grid(column=1, row=1)

ttk.Label(frame, text="By Tomiwa Shobowale and Oghenetega Gbejewoh").grid(column=0, columnspan=2, row=2); # Credits

root.mainloop()
