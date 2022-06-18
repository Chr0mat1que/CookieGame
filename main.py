from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("800x600")

#frame = ttk.Frame(root)

desc = ttk.Label(root, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", wraplength=500,  justify="center") # This is the description text, stating what the game is about and other important information.
desc.place(anchor=CENTER, relx=0.5, rely=0.2);

start_btn = ttk.Button(root, text="Start")
start_btn.place(anchor=CENTER, relx=0.5, rely=0.47)
exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.place(anchor=CENTER, relx=0.5, rely=0.53)

ttk.Label(root, text="By Tomiwa Shobowale and Oghenetega Gbejewoh").place(anchor=CENTER, relx=0.5, rely=0.95) # Credits

root.mainloop()
