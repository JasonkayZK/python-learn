""" Scale

Scale 一个滑块控件。用于在一个范围内，拖动它改变值的大小，例如音量条。

"""

from tkinter import *

root = Tk()
v = IntVar()
# from_ : 设置最小值  to：设置最大值
# tickinterval：设置刻度   length：设置滑块的长度，单位为像素
Scale(root, orient='horizontal',
      variable=v,
      from_=0,
      to=200,
      tickinterval=50,
      length=200).pack()

root.mainloop()
