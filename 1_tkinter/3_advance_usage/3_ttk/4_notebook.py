""" Notebook

选项卡控件

"""

import tkinter as tk
from tkinter.ttk import *

root = tk.Tk()
root.geometry("300x300")

notebook = Notebook(root)

page1 = tk.Frame(notebook, background="yellow")
Label(page1, text="这是 tab1 的界面").pack()

page2 = tk.Frame(notebook, background="pink")
Label(page2, text="这是 tab2 的界面").pack()

notebook.add(page1, text="Tab1")
notebook.add(page2, text="Tab2")
notebook.pack(fill=tk.BOTH, expand=1)

root.mainloop()
