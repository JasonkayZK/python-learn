"""

无参数

"""

import tkinter as tk


def callback():
    print("被点击了")


root = tk.Tk()
tk.Button(root, text="单击", command=callback).pack()

root.mainloop()
