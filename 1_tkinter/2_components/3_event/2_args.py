"""

有参数

"""

import tkinter as tk


def callback(args):
    print("被点击了", args)


root = tk.Tk()
tk.Button(root, text='单击', command=lambda: callback("按钮")).pack()

root.mainloop()
