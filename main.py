from tkinter import *
from tkinter import ttk

root = Tk(className="Cookie")
root.geometry("800x600")

frame = ttk.Frame(root)
frame.place(anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1);

title_lbl = ttk.Label(frame, text="Cookie", font=("Arial, 25"))
title_lbl.place(anchor=CENTER, relx=0.5, rely=0.1);

desc_lbl = ttk.Label(frame, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", wraplength=500,  justify="center") # This is the description text, stating what the game is about and other important information.
desc_lbl.place(anchor=CENTER, relx=0.5, rely=0.3)

start_btn = ttk.Button(frame, text="Start")
start_btn.place(anchor=CENTER, relx=0.5, rely=0.47)
exit_btn = ttk.Button(frame, text="Exit", command=root.destroy)
exit_btn.place(anchor=CENTER, relx=0.5, rely=0.53)

credits_lbl = ttk.Label(frame, text="By Tomiwa Shobowale and Oghenetega Gbejewoh")
credits_lbl.place(anchor=CENTER, relx=0.5, rely=0.95)

root.mainloop()
