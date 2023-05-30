import tkinter as tk
from tkinter import filedialog
import subprocess

def select_file():
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=[("Video files", "*.mp4 *.avi *.mkv"), ("All files", "*.*")]
    )
    subprocess.run(["python", "main.py", file_path])

window = tk.Tk()
file_button = tk.Button(
    window, text="Select a video file", command=select_file)
file_button.pack()
window.mainloop()
