""" Checkbutton

Checkbutton 一个多选框组件。主要给用户提供多个选项的选中功能。

w= Checkbutton(parent，option，...)

方法	描述
deselect()	清除单选按钮的状态
flash()	在激活状态颜色和正常颜色之间闪烁几次单选按钮，但保持它开始时的状态。
invoke()	可以调用此方法来获得与用户单击单选按钮以更改其状态时发生的操作相同的操作
select()	设置单选按钮为选中。
toggle()	反选。当前被选中，则调用之后变为未选中，反之则为选中。

"""

from tkinter import *


def sel():
    val = "Checkbutton value is " + str(v.get())
    print(val)


root = Tk()
v = IntVar()
c = Checkbutton(root, text="点我啊", variable=v, command=sel)
c.select()
c.pack()
root.mainloop()
