""" Label

Label 一个标签组件。主要用来实现显示功能，可以显示文字和图片。

l = Label(parent, option=value ... ) 参数说明：

parent: 代表承载该按钮的父容器.
options: 可选项，即该按钮的可设置的属性。这些选项可以用键 =值的形式设置，并以逗号分隔

关于图片显示

注意：Python内置了10种位图，可以直接使用，设置bitmap属性即可。

"error" "gray75" "gray50" "gray25" "gray12" "hourglass" "info" "questhead" "question" "warning"
"""

from tkinter import *

root = Tk()
Label(root, text="我是标签").pack()
Label(root, bitmap="questhead").pack()
Label(root, bitmap="hourglass").pack()
root.mainloop()
