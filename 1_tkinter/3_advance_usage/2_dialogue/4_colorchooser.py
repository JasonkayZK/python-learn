""" colorchooser

颜色选择对话框

"""

from tkinter import *
from tkinter import colorchooser


def onclick():
    file_name = colorchooser.askcolor()

    # 返回值是一个元组，第一个元素是RGB色值元组，第二个是对应的16进制色值
    print(file_name)


root = Tk()

Button(root, text="选色", command=onclick).pack()

root.mainloop()
