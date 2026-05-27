"""
Graphical User Interface for the
M122 File Organizer project.

Responsibilities:
- Start file processing
- Display detected/moved files
- Show progress
- Display status information
- Provide user interaction
"""

import tkinter as tk
from tkinter import ttk

from detector import scan_folder
from parser import extract_module
from mover import move_file
from config import DOWNLOADS_PATH


def update_status(message):
    """
    Update status label text.

    Args:
        message (str):
            Status message
    """

    status_label.config(
        text=message
    )

    root.update_idletasks()


def reset_interface():
    """
    Reset GUI elements.
    """

    progress["value"] = 0

    file_list.delete(
        0,
        tk.END
    )


def process_files(files):
    """
    Process detected files.

    Args:
        files (list):
            List of files
    """

    total_files = len(files)

    progress["maximum"] = total_files


    for index, file in enumerate(files):

        module = extract_module(
            file.name
        )


        moved_file = move_file(
            file,
            module
        )


        file_list.insert(
            tk.END,
            f"✓ {file.name}"
        )


        progress["value"] = (
            index + 1
        )


        percentage = int(
            ((index + 1) / total_files)
            * 100
        )


        update_status(
            f"Progress: {percentage}%"
        )


def start_sorting():
    """
    Start sorting workflow.
    """

    start_button.config(
        state="disabled",
        text="Sorting..."
    )


    try:

        reset_interface()


        files = scan_folder(
            DOWNLOADS_PATH
        )


        if len(files) == 0:

            update_status(
                "No files found"
            )

            return


        update_status(
            "Sorting files..."
        )


        process_files(
            files
        )


        update_status(
            f"✓ Finished ({len(files)} files moved)"
        )


    except Exception as error:

        update_status(
            f"❌ {error}"
        )


    finally:

        start_button.config(
            state="normal",
            text="Start File Sorting"
        )


"""
Main window
"""

root = tk.Tk()

root.iconbitmap(
    "../assets/icon.ico"
)

root.title(
    "M122 File Organizer"
)

root.geometry(
    "800x550"
)

root.configure(
    bg="#202124"
)


"""
Title
"""

title = tk.Label(
    root,
    text="M122 File Organizer",
    font=("Arial",20,"bold"),
    bg="#202124",
    fg="#ffffff"
)

title.pack(
    pady=20
)


"""
Start button
"""

start_button = tk.Button(
    root,
    text="Start File Sorting",
    command=start_sorting,
    bg="#4285F4",
    fg="white",
    font=("Arial",11),
    width=25
)

start_button.pack(
    pady=10
)


"""
Progress bar
"""

progress = ttk.Progressbar(
    root,
    length=600
)

progress.pack(
    pady=20
)


"""
File list
"""

file_list = tk.Listbox(
    root,
    width=90,
    height=15,
    bg="#303134",
    fg="#ffffff",
    font=("Consolas",10)
)

file_list.pack(
    pady=15
)


"""
Status label
"""

status_label = tk.Label(
    root,
    text="Waiting...",
    bg="#202124",
    fg="#8ab4f8",
    font=("Arial",11)
)

status_label.pack()


root.mainloop()