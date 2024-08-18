""" 事件与绑定

所谓事件，就是在用户按下一个键或点击鼠标时，应用程序需要做出的反应。

简单说就是对外部刺激做出的反应。

当窗口小控件中注册的事件发生时，会回调关联的处理函数，

并将事件对象的实例作为参数传递到这个处理函数中。


# 常用的几个鼠标事件

- <Button-1>：鼠标左击事件
- <Button-2>：鼠标滚轮点击
- <Button-3>：鼠标右击事件
- <Double-Button-1>：鼠标左双击事件
- <Triple-Button-1>：鼠标左三击事件

"""

import tkinter as tk


def callback(event):
    print("EventType=", event.type)
    print("Num=", event.num)


def callback_args(event, a, b):
    print(a, b)
    print("EventType=", event.type)
    print("Num=", event.num)


root = tk.Tk()
l = tk.Label(root, text='单击')
l.bind("<Double-Button-1>", callback)
l.pack()

frame = tk.Frame(root, bg='khaki', width=100, height=80)
frame.bind("<Button-1>", lambda event: callback_args(event, 1, 2))
frame.pack()

root.mainloop()
