""" Combobox

输入框下拉选项菜单

"""

from tkinter import *
from tkinter import ttk


def selected_item(_event):
    selected_value = combo.get()
    print("Selected item:", selected_value)


root = Tk()

# 创建一个字符串变量来储存选择的值
selected_var = StringVar()

# 创建 Combobox
combo = ttk.Combobox(root, textvariable=selected_var)
combo["values"] = ("Option 1", "Option 2", "Option 3", "Option 4")
combo.bind("<<ComboboxSelected>>", selected_item)

# 设置默认选项
combo.current(0)

# 设置布局
combo.pack(pady=10)

root.mainloop()
