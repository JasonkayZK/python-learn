""" filedialog

参数说明：

- title: 设置文件对话框的标题

- initialdir: 设置默认打开的路径

- filetypes: 文件类型筛选。

它的值是一个列表，列表中的元素必须是一个二元元组。
元组的第一个元素是类型名称，第二个是类型后缀名。

"""

from tkinter import *
from tkinter import filedialog


def onclick():
    file_name = filedialog.askopenfilename(
        title="打开我的文件", initialdir="D:\\", filetypes=[("PNG", ".png"), ("文本文档", ".txt")]
    )
    print(file_name)


def save_file():
    file_name = filedialog.asksaveasfilename(title="保存文件", initialdir="D:\\")
    print(file_name)


root = Tk()

Button(root, text="浏览", command=onclick).pack()
Button(root, text="保存", command=save_file).pack()

root.mainloop()
