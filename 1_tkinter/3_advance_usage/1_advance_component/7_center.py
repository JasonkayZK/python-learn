""" 窗口居中的方法

注意，当窗口大小不固定时，是通过动态获取根窗口的宽高来计算位置

如果窗口的宽高一开始就是确定的，请使用确定值，尽量避免动态获取窗口的大小，以免影响GUI的流畅。

"""

from tkinter import *

root = Tk()

# 获取当前根窗口的宽、高
cur_width = root.winfo_width()
cur_height = root.winfo_height()

# 获取电脑屏幕的宽、高
scn_width, scn_height = root.maxsize()

# 窗口显示的坐标拼接成固定格式字符串
tmpcnf = "+%d+%d" % ((scn_width - cur_width) / 2, (scn_height - cur_height) / 2)

root.geometry(tmpcnf)

# 固定窗口的长宽，不可改变窗口大小(width=None, height=None)
root.resizable(False, False)

Label(root, text="我是标签", bg="yellow").pack(side=LEFT)
Button(root, text="这是按钮").pack(side=LEFT)

root.mainloop()
