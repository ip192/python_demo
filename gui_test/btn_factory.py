import tkinter as tk
# from gui_test.run_shells import cd_to

def _btn_click(item):
    pass
    # print(item)
    # cd_to(item)

def make_btn(window, content = []):
    for txt in content:
        btn = tk.Button(window, text=txt, width='40', height='10', command=_btn_click)
        btn.pack()


