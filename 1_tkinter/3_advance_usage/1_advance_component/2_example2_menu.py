""" Menu

参数说明：

tearoff

菜单项列表中的第一个位置（位置0）会被一个“脱离”元素占用，tearoff=0时，菜单将没有脱离功能

accelerator

在菜单项名称的右侧显示一个快捷键提示。注意，它只是一个提示，快捷键功能需要监听按键来实现。

"""

from tkinter import Menu, Tk

root = Tk()

# 创建窗口顶部的菜单栏对象
menu_bar = Menu(root)
# 将菜单栏对象设置给根窗口
root["menu"] = menu_bar  # 等价于 root.config(menu=menu_bar)

# 创建“文件”联级菜单
file_menu = Menu(menu_bar, tearoff=0)
# 在菜单栏上添加菜单标签，并将该标签与相应的联级菜单关联起来
menu_bar.add_cascade(label="文件", menu=file_menu)

# 在文件联级菜单中添加菜单项
file_menu.add_command(label="新建", accelerator="Ctrl+N")
file_menu.add_command(label="打开", accelerator="Ctrl+O")
file_menu.add_command(label="保存", accelerator="Ctrl+S")
# 添加分割线
file_menu.add_separator()
file_menu.add_command(label="退出", accelerator="Alt+F4")

about_menu = Menu(menu_bar, tearoff=1)
menu_bar.add_cascade(label="关于", menu=about_menu)
about_menu.add_command(label="关于")
about_menu.add_command(label="帮助")

root.mainloop()
