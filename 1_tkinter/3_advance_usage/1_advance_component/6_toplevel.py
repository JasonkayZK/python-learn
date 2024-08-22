""" Toplevel

实际上我们的根窗口就是一个顶级窗口。

它是独立存在的一个窗口，当我们需要编写多窗口程序或者自定义对话框时，就需要使用它。


# 关于geometry的参数设置

该方法需要传入一个固定格式的字符串，格式："wxh±x±y":

- 其中w、h表示窗口的宽和高
- x、y表示窗口显示位置的横向和纵向坐标
- +、-则表示正方向还是负方向，基于屏幕左上角为坐标原点，向下或向右为正方向。

"""

from tkinter import *


def window_test(window):
    # 让窗口最小化
    window.iconify()
    # 将最小化的窗口显示出来
    # window.deiconify()

    # 销毁窗口
    # window.destroy()
    # 退出mainloop循环
    # window.quit()


def onclick():
    window = Toplevel()
    # 设置窗口出现的位置
    window.geometry("+300+300")
    window.title("子窗口")

    # 该方法传入True时，去除窗口边框
    # window.overrideredirect(True)
    Button(window, text="点你妹", command=lambda: window_test(window)).pack()

    # 设置所依托的父窗口
    # window.transient(root)
    # 必须要加上此行，打开一个新窗口后，必须进入新窗口的事件循环
    window.mainloop()


root = Tk()

# 设置窗口标题
root.title("主窗口")

# 设置窗口的宽高与显示的位置
root.geometry("300x200+200+200")

# 固定窗口的长宽，不可改变窗口大小(width=None, height=None)
root.resizable(False, False)

# 设置窗口小图标(必须位于geometry与resizable方法之后)
root.iconbitmap("avatar.ico")

Button(root, text="打开窗口", command=onclick).pack()

root.mainloop()
