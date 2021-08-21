import tkinter as tk
from tkinter import ttk
from tkinter import *
import joinClass
import subprocess
import time
import config

def signIn(subject):
    root.iconify()
    time.sleep(2)
    subprocess.call([config.zoom_location, "--kiosk"])
    joinClass.sign_in(subject)

root = tk.Tk()
root.title('Zoom Bot Application')

# Variables for Font, Images, etc.
Font_heading = ("Cooper Std Black", 20, "bold")
Font_subjects = ("Cooper Std Black", 15, "bold")
join_icon = tk.PhotoImage(file='./Assets/join.png')
zoom_ico = "./Assets/zoom.ico"
#Edit your subjects (this will be displayed in the GUI)
sub = ["Accountancy", "Business", "Arts", "English", "Moral Science", "Economics",
       "Accountancy", "Business", "Arts", "English", "Moral Science", "Economics"] 


# setting the window
window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.iconbitmap(zoom_ico)

# heading
topMsg = "Click on the join button to join the class"
message = tk.Label(root, text=topMsg, font =  Font_heading)
message.pack()

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)


# create frames
frame1 = ttk.Frame(notebook, width=590, height=300)
frame2 = ttk.Frame(notebook, width=590, height=300)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)


notebook.add(frame1, text='Frame-1')
notebook.add(frame2, text='Frame-2')

# create content in frame
for i in range(6):
    ttk.Label(frame1, font = Font_subjects,
              text = sub[i]).grid(column = 0,row = i,padx = 50, pady = 10, sticky = "W")
    join_btn = ttk.Button(
        frame1, text = i,
        image = join_icon,
        command = lambda temp = i : signIn(sub[temp])
    ).grid(column = 2, row = i, padx = 210,sticky = "E")
    ttk.Label(frame2, font = Font_subjects,
        text = sub[i+6]).grid(column = 0, row = i,padx = 50,pady = 10, sticky = "W")
    join_btn = ttk.Button(
        frame2,
        image = join_icon,
        command = lambda temp = i : signIn(sub[temp])
    ).grid(column = 2, row = i, padx = 210,sticky = "E")

if __name__ == "__main__":
    root.mainloop()
