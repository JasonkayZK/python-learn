"""

不使用lambda表达式

命令绑定的缺陷：

- 只有Button和一小部分控件支持
- 功能单一。命令只能绑定到鼠标左键单击和空格键点击事件，无法实现焦点、鼠标滚轮、快捷键响应等等丰富的交互情况

"""

import tkinter as tk


class Command:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def callback(args):
    print("被点击了", args)


root = tk.Tk()
tk.Button(root, text="单击", command=Command(callback, "按钮")).pack()

root.mainloop()
