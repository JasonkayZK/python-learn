""" Grid

网格布局，是最被推荐使用的布局。

程序大多数都是矩形的界面，我们可以很容易把它划分为一个几行几列的网格，

然后根据行号和列号，将组件放置于网格之中。

使用grid 布局时，需要在里面指定两个参数，分别用row 表示行，column 表示列。

需要注意的是 row 和 column 的序号都从0 开始，且每个网格只能容纳一个窗口小控件。

使用grid布局前，要打好腹稿，将界面划分成网格状

"""

from tkinter import *

root = Tk()

Label(root, width=15, height=3, bg="red").grid(row=0, column=0)
Label(root, width=15, height=3, bg="green").grid(row=0, column=1)
Label(root, width=15, height=3, bg="blue").grid(row=0, column=2)
Label(root, width=15, height=3, bg="white").grid(row=1, column=0)
Label(root, width=15, height=3, bg="black").grid(row=1, column=1)
Label(root, width=15, height=3, bg="grey").grid(row=1, column=2)

root.mainloop()
