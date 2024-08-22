"""
# Listbox 列表框通常用于数据展示或者作为选项菜单使用。

参数说明：

selectmode 设置列表框的选择模式。共有四个值:

- SINGLE表示单选
- BROWSE也是单选但该模式可以通过拖动鼠标来单选，而不仅仅只是点击。
- MULTIPLE表示多选
- EXTENDED则表示可以通过拖动鼠标来多选，当然，也可以配合Shift键通过点击来多选。

selectmode属性默认值是BROWSE。

参数说明：

- yscrollcommand: 列表框纵向滚动时的回调监听，该属性的值是一个回调函数
- xscrollcommand: 列表框横向滚动时的回调监听。


# Scrollbar 滚动条则是一种辅助的小控件，它通常与列表框或者多行文本框结合使用。

Scrollbar 参数说明：

- command：滚动条拖动时的回调监听，其属性值是一个回调函数

"""

from tkinter import *

root = Tk()

# 创建列表框
list_box = Listbox(root, height=5)

# 添加列表项到 Listbox
items = ["Go", "Python", "Java", "Dart", "JavaScript", "C", "C++", "PHP"]
for item in items:
    list_box.insert(END, item)

# 分别创建x方向、y方向的两个滚动条。orient属性设置其滚动方向
y_bar = Scrollbar(root, orient=VERTICAL)
x_bar = Scrollbar(root, orient=HORIZONTAL)

# 设置滚动条的命令和Listbox的滚动视图
list_box.config(yscrollcommand=y_bar.set, xscrollcommand=x_bar.set)
y_bar.config(command=list_box.yview)
x_bar.config(command=list_box.xview)

# 设置布局方位
y_bar.pack(side=RIGHT, fill=Y)
x_bar.pack(side=BOTTOM, fill=X)
list_box.pack(anchor=NW, fill=BOTH, expand=YES)

root.mainloop()
