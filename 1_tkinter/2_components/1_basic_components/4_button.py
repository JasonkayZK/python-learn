""" Button

Button 一个简单的按钮，用来响应用户的一个点击操作。
能够与一个函数关联，当按钮被按下时，自动调用该函数。
它的属性可以直接参考标签，事实上按钮就是一个特殊的标签，只不过按钮多出了点击响应的功能

b = Button(parent,option=value,... )

"""

from tkinter import *


def onclick():
    print("点你妹啊 ")


root = Tk()
Button(root, text="按钮", command=onclick).pack()
root.mainloop()
