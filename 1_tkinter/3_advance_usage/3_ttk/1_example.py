""" TTK的使用

如果是使用from tkinter import * 方式导包，

则只需在其下增加from tkinter.ttk import * 即可应用ttk风格。

使用ttk模块后，小控件外观会产生差别。


如使用其他方式导包，则需指定ttk模块控件!


ttk仅支持11个原核心控件:

Button
Checkbutton
Entry
Frame
Label
LabelFrame
Menubutton
PanedWindow
Radiobutton
Scale
Scrollbar

"""

from tkinter import *

# 增加如下导包语句即可
from tkinter.ttk import *

root = Tk()
root.geometry("300x300")

top = LabelFrame(root, text="Label")
top.pack(padx=8, pady=8)
Label(top, text="我是标签，哈哈").pack()

body = LabelFrame(root, text="Button")
body.pack(padx=8, pady=8)
Button(body, text="你点啊").pack()

bottom = LabelFrame(root, text="其他")
bottom.pack(padx=8, pady=8)
Checkbutton(bottom, text="唱歌").pack()
Checkbutton(bottom, text="跳舞").pack()
Checkbutton(bottom, text="健身").pack()

Scale(bottom, orient="horizontal", from_=0, to=100).pack()

root.mainloop()
