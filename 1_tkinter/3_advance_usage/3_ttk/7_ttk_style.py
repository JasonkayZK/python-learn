""" 设置主题与样式

在使用ttk控件时，会发现它的控件不支持 bg、fg、border 这样涉及样式的属性

这是因为它对外观样式进行了重新定义。

ttk 对外观样式的抽象共有三个级别:

- 主题
- 样式
- 状态样式

"""

from tkinter import ttk

style = ttk.Style()
# 获取所有支持的主题
print(style.theme_names())

# 获取当前使用的主题
print(style.theme_use())

# 切换主题
style.theme_use("classic")
