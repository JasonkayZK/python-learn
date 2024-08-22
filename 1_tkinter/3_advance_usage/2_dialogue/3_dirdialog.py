""" 选择文件夹对话框

选择文件夹对话框，这个在tkinter文档中没有写，但是通过查看源码可以找到

"""

from tkinter import *
from tkinter import filedialog


def onclick():
    # 选择文件夹对话框
    file_name = filedialog.askdirectory(initialdir="D:\\")
    print(file_name)


root = Tk()

Button(root, text="浏览", command=onclick).pack()

root.mainloop()
