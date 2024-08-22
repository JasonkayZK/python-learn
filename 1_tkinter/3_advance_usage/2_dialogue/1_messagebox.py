""" messagebox

消息对话框

"""

from tkinter import *
from tkinter import messagebox

root = Tk()

# 设置窗口标题
root.title("主窗口")

# parent指定依托的父窗口，若不指定，默认为根窗口
result = messagebox.askokcancel("标题", "这是内容", parent=root)
print(result)

messagebox.askquestion("标题", "这是question窗口")
messagebox.askretrycancel("标题", "这是retry cancel窗口")
messagebox.showerror("标题", "这是error窗口")
messagebox.showinfo("标题", "这是info窗口")
messagebox.showwarning("标题", "这是warning窗口")

root.mainloop()
