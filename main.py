from tkinter import *
from tkinter import ttk
import scenes


root = None
mainmenu_frame = None
mysterymenu_frame = None
images = []

def init_root():
    global root
    root = Tk(className="Cookie")
    root.geometry("800x600")

def close_mainmenu():
    global mainmenu_frame
    if mainmenu_frame != None:
        mainmenu_frame.destroy()
        mainmenu_frame = None

def create_mysterymenu(tag="0"):
    global mainmenu_frame
    global mysterymenu_frame
    global root
    close_mainmenu()
    close_mysterymenu()

    mysterymenu_frame = ttk.Frame(root)
    mysterymenu_frame.place(anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1) 

    for scene in scenes.scenes:
        if scene["tag"] == tag: 
            image_frame = ttk.Frame(mysterymenu_frame)
            image_frame.place(anchor=CENTER, relx = 0.5, rely = 0.15)
            
            # Add images, maximum of 6 currently
            if len(scene["images"]) > 0:
                image0 = PhotoImage(file="./images/" + scene["images"][0] + ".png")
                ttk.Label(image_frame, image=image0).grid(column=0, row=0)
 
            if len(scene["images"]) > 1:
                image1 = PhotoImage(file="./images/" + scene["images"][1] + ".png")
                ttk.Label(image_frame, image=image1).grid(column=1, row=0)

            if len(scene["images"]) > 2:
                image2 = PhotoImage(file="./images/" + scene["images"][2] + ".png")
                ttk.Label(image_frame, image=image2).grid(column=2, row=0)

            if len(scene["images"]) > 3:
                image3 = PhotoImage(file="./images/" + scene["images"][3] + ".png")
                ttk.Label(image_frame, image=image3).grid(column=3, row=0)

            if len(scene["images"]) > 4:
                image4 = PhotoImage(file="./images/" + scene["images"][4] + ".png")
                ttk.Label(image_frame, image=image4).grid(column=4, row=0)

            if len(scene["images"]) > 5:
                image5 = PhotoImage(file="./images/" + scene["images"][5] + ".png")
                ttk.Label(image_frame, image=image5).grid(column=5, row=0)
            
            desc_lbl = ttk.Label(mysterymenu_frame, text=scene["description"], wraplength=500)
            desc_lbl.place(anchor=CENTER, relx=0.5, rely=0.45)

            a_btn = ttk.Button(mysterymenu_frame, text=scene["a"], command=lambda _tag = scene["a_next"]: create_mysterymenu(_tag))
            a_btn.place(anchor=CENTER, relx=0.5, rely="0.7")
            
            b_btn = ttk.Button(mysterymenu_frame, text=scene["b"], command=lambda _tag = scene["b_next"]: create_mysterymenu(_tag))
            b_btn.place(anchor=CENTER, relx=0.5, rely="0.75")
            
            c_btn = ttk.Button(mysterymenu_frame, text=scene["c"], command=lambda _tag = scene["c_next"]: create_mysterymenu(_tag))
            c_btn.place(anchor=CENTER, relx=0.5, rely="0.8")
            
            credits_lbl = ttk.Label(mainmenu_frame, text="By Tomiwa Shobowale, Oghenetega Gbejewoh and Kamsi Onubogu")
            credits_lbl.place(anchor=CENTER, relx=0.5, rely=0.95)
            root.mainloop()


def close_mysterymenu():
    global mysterymenu_frame
    if mysterymenu_frame != None:
        mysterymenu_frame.destroy()
        mysterymenu_frame = None

def create_mainmenu():
    global mainmenu_frame
    mainmenu_frame = ttk.Frame(root)
    mainmenu_frame.place(anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1);
    
    title_lbl = ttk.Label(mainmenu_frame, text="Cookie", font=("Arial, 25"))
    title_lbl.place(anchor=CENTER, relx=0.5, rely=0.1);
    
    desc_lbl = ttk.Label(mainmenu_frame, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", wraplength=500,  justify="center") # This is the description text, stating what the game is about and other important information.
    desc_lbl.place(anchor=CENTER, relx=0.5, rely=0.3)
    
    start_btn = ttk.Button(mainmenu_frame, text="Start", command=create_mysterymenu)
    start_btn.place(anchor=CENTER, relx=0.5, rely=0.47)
    exit_btn = ttk.Button(mainmenu_frame, text="Exit", command=root.destroy)
    exit_btn.place(anchor=CENTER, relx=0.5, rely=0.53)
    
    credits_lbl = ttk.Label(mainmenu_frame, text="By Tomiwa Shobowale and Oghenetega Gbejewoh")
    credits_lbl.place(anchor=CENTER, relx=0.5, rely=0.95)

def main():
    init_root()
    create_mainmenu() 
    root.mainloop()

main()
