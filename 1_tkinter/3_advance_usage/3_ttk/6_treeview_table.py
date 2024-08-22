"""

用 Treeview 制作表格

Treeview 参数说明：

- show: 用于禁止列顶部标签。
有两个值，'tree'表示禁止每一列的顶部标签栏，'headings'表示禁止首列显示。

"""

import tkinter as tk
from tkinter import ttk


def item_select(_event):
    for select in tree.selection():
        print(tree.item(select, "values"))


def head_onclick(ttype):
    print(ttype)


root = tk.Tk()

# show用于禁止列顶部标签。columns用于设置每一列的列标识字符串
tree = ttk.Treeview(root, show="headings", columns=["0", "1", "2"])

# 监听tree中item被选中的事件
tree.bind("<<TreeviewSelect>>", item_select)

# 设置表头名称
tree.heading(0, text="序号", command=lambda: head_onclick("序号"))
tree.heading(1, text="姓名", command=lambda: head_onclick("姓名"))
tree.heading(2, text="年龄", command=lambda: head_onclick("年龄"))

# 设置每列中元素的样式
tree.column(0, anchor="center")
tree.column(1, anchor="center")
tree.column(2, anchor="center")

# "end" 表示往父节点的最后一个位置插入
tree.insert("", "end", values=("1", "赵二", "19"))
tree.insert("", "end", values=("2", "张三", "20"))
tree.insert("", "end", values=("3", "李四", "22"))
tree.insert("", "end", values=("4", "王五", "18"))

tree.pack()
root.mainloop()
