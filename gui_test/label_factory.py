
import tkinter as tk

def make_label(window, content = []):
    for txt in content:
        label = tk.Label(window, text = txt)
        label.pack()

