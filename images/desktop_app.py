import asyncio
import threading
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory, askopenfilenames
from tkinter.messagebox import showerror

from functions import convert_all_to_png


class JPEGToPNGWindow(Toplevel):

    def __init__(
        self, master=None, callback=None, callback_args=(), *args, **kwargs
    ) -> None:
        super().__init__(master, *args, **kwargs)
        self.geometry("720x480")
        self.title("JPEG to PNG Converter")
        self.focus()

        main_frame = ttk.Frame(self)
        main_frame.grid(row=0, column=0)

        ttk.Button(
            main_frame, text="Choose files", command=self.open_files_selection
        ).grid(column=0, row=0, pady=20, padx=5)
        self.preview_image_paths = Text(
            main_frame, width=60, height=15, state="disabled"
        )
        self.preview_image_paths.grid(column=1, row=0, pady=20)

        ttk.Button(
            main_frame, text="Where to save", command=self.open_destination_folder
        ).grid(column=0, row=1, pady=20, padx=10)
        self.preview_dest_path = Text(main_frame, width=60, height=3, state="disabled")
        self.preview_dest_path.grid(column=1, row=1, pady=20)

        self.convert_btn = ttk.Button(main_frame, text="Convert", command=self.convert)
        self.convert_btn.grid(column=0, row=2, pady=20)

        self.callback = callback
        self.callback_args = callback_args
        self.dest_folder = None
        self.filenames = ()

    def open_files_selection(self):
        filetypes = (("Image files", (".jpg", ".jpeg")),)
        filenames = askopenfilenames(
            filetypes=filetypes, title="Select image(s)", initialdir="~/Downloads"
        )

        self.preview_image_paths["state"] = "normal"
        self.preview_image_paths.delete(1.0, END)

        for filename in filenames:
            self.preview_image_paths.insert(END, filename + "\n")

        self.preview_image_paths["state"] = "disabled"
        self.filenames = filenames

    def open_destination_folder(self):
        dest_folder = askdirectory(title="Save in folder")
        if dest_folder:
            self.preview_dest_path["state"] = "normal"
            self.preview_dest_path.insert(1.0, dest_folder)
            self.preview_dest_path["state"] = "disabled"
            self.dest_folder = dest_folder

    def convert(self):
        if len(self.filenames) < 1:
            return showerror("File(s) not found", "Can not convert without image(s)")

        if self.dest_folder is None:
            return showerror(
                "Folder not found", "Please choose a folder to save an image"
            )

        self.convert_btn["text"] = "Converting..."
        self.convert_btn["state"] = "disabled"

        thread = threading.Thread(
            target=convert_all_to_png, args=(self.filenames, self.dest_folder)
        )
        thread.start()
        thread.join()

        self.convert_btn["text"] = "Convert"
        self.convert_btn["state"] = "normal"

    def destroy(self) -> None:
        super().destroy()
        if self.callback:
            self.callback(*self.callback_args)


class MainWindow(Tk):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title("Image Utilities")
        self.geometry("400x100")

        main_frame = ttk.Frame(self)
        jpeg_to_png_btn = ttk.Button(
            main_frame,
            text="JPEG to PNG",
            command=self.open_jpeg_to_png_converter_window,
        )
        jpeg_to_png_btn.grid(column=0, row=0, padx=10, pady=10)

        remove_exif_btn = ttk.Button(main_frame, text="Remove Exif")
        remove_exif_btn.grid(column=1, row=0, padx=10, pady=10)

        main_frame.pack(expand=1, fill="both")

        self.secondary_window = None

    def _clear_secondary_window_flag(self):
        self.secondary_window = None

    def open_jpeg_to_png_converter_window(self):
        if not self.secondary_window:
            self.secondary_window = JPEGToPNGWindow(
                callback=self._clear_secondary_window_flag
            )


MainWindow().mainloop()
