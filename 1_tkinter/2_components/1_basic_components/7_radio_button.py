""" Radiobutton

Radiobutton 单选按钮，即在同一组内只能有一个按钮被选中

每当选中组内的一个按钮时，其它的按钮自动改为非选中态

与其他控件不同的是，它有组的概念。

w = Radiobutton(parent, option, ... )

方法	描述
deselect()	清除单选按钮的状态
flash()	在激活状态颜色和正常颜色之间闪烁几次单选按钮，但保持它开始时的状态。
invoke()	可以调用此方法来获得与用户单击单选按钮以更改其状态时发生的操作相同的操作
select()	设置单选按钮为选中。

"""

from tkinter import *


def sel():
    selection = "You selected the option " + str(var.get())
    print(selection)


root = Tk()

# 创建整型变量，用于绑定，相同的整型变量是为同一组
var = IntVar()
Radiobutton(root, text="Option 1", variable=var, value=1, command=sel).pack(anchor=W)
Radiobutton(root, text="Option 2", variable=var, value=2, command=sel).pack(anchor=W)
Radiobutton(root, text="Option 3", variable=var, value=3, command=sel).pack(anchor=W)

root.mainloop()
