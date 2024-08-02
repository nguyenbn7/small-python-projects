import asyncio
import threading
from tkinter import Tk, ttk
from tkinter.filedialog import askdirectory, askopenfile
from tkinter.messagebox import showerror

import __init__

from src.images.converters import convert_to_png

window = Tk()
window.title("Convert JPEG Image to PNG Image")
window.geometry("640x480")

source = None
dest = None


def open_file_selection():
    filetypes = (("Image files", (".jpg", ".jpeg")),)
    file = askopenfile(
        filetypes=filetypes, title="Choose an image", initialdir="~/Downloads"
    )
    if file:
        display_file_name["text"] = file.name
        global source
        source = file.name


def save_file_selection():
    path = askdirectory(title="Save folder")
    if path:
        display_save_file_name["text"] = path
        global dest
        dest = path


def convert():
    if source is None:
        return showerror("File is empty", "Can not convert without an image")

    if dest is None:
        return showerror("Path not found", "Please choose a path to save an image")

    th = threading.Thread(target=convert_to_png, args=(source, dest))
    th.start()
    th.join()
    print(th.is_alive())


main_frame = ttk.Frame(window, padding=10)
main_frame.grid()

display_file_name = ttk.Label(main_frame, justify="left")
display_file_name.grid(column=1, row=0)

ttk.Button(main_frame, text="Choose a file", command=open_file_selection).grid(
    column=0, row=0, pady=20
)


display_save_file_name = ttk.Label(main_frame, justify="left")
display_save_file_name.grid(column=1, row=1)
ttk.Button(main_frame, text="where to save", command=save_file_selection).grid(
    column=0, row=1, pady=20
)

convert_button = ttk.Button(main_frame, text="convert", command=convert)
convert_button.grid(column=0, row=2, pady=20)

window.mainloop()
