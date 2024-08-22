""" Treeview

树形控件

"""

import tkinter as tk
from tkinter import ttk


def item_select(_event):
    for select in tree.selection():
        print(tree.item(select, "text"))


root = tk.Tk()
tree = ttk.Treeview(root, show="tree")

# 监听tree中item被选中的事件
tree.bind("<<TreeviewSelect>>", item_select)

# 第一个参数为父节点, 第二个为此项在父节点中的位置（父节点为空时，默认为根节点）
item1 = tree.insert("", 0, text="广东省")

# 在第一个节点中插入如下子节点
tree.insert(item1, 0, text="广州市")
tree.insert(item1, 1, text="深圳市")

item2 = tree.insert("", 1, text="湖北省")
tree.insert(item2, 0, text="武汉市")

tree.pack()
root.mainloop()
