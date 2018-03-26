import tkinter as tk


class list_box(window=tk.Listbox, content = []):
    def __init__(self, window, content):
        self.make_list(window, content)

    def make_list(window, content):
        lb = tk.Listbox(window, width = '200', height = '200')
        for item in content:
            lb.insert(tk.END, item)
        lb.pack()

    def click_event(self, event):
        print(event.widget)
        print(self.grab_current())