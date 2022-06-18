import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("800x800")
frame = ttk.Frame(root)
frame.pack()

canvas = tkinter.Canvas(root, height=700, width=700, bg="#ffffcc")
canvas.pack()

canvas.create_text(350, 50, text="Cookie Breaker", fill="black", font=('Helvetica 15 bold'))
canvas.pack()

canvas.create_text(350, 150, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", fill="black", font=('Helvetica 12 bold'), width=500) # This is the description text, stating what the game is about and other important information.canvas.pack()


start_btn = ttk.Button(canvas, text="Start")
exit_btn = ttk.Button(canvas, text="Exit", command=root.destroy)

ttk.Label(canvas, text="By Oluwatomiwa Shobowale and Oghenetega Gbejewoh")# Credits

canvas.create_text(350, 650, text="By Oluwatomiwa Shobowale and Oghenetega Gbejewoh", fill="black", font=('Helvetica 15 bold'))
canvas.pack()
root.mainloop()
