""" 事件属性（Event类）

char    键盘事件，按键的字符
delta   鼠标滚动事件，鼠标滚动的距离
height、width 仅用于Configure事件,即当控件形状发生变化之后的宽度和高度.相当于SizeChanged事件
keycode     键盘事件，按键码
keysym、 keysym_num 按键事件
num 鼠标事件，鼠标按键码，1为左键，2为中建，3为右键
serial 相当于Event的ID
state 用来表示修饰键的状态,即ctrl,shift,alt等修饰键的状态.
time 事件发生的时间
type 事件的类型
widget 事件源控件
x、y，x_root、y_root 鼠标事件中鼠标的位置。x_root、·y_root`为绝对坐标，x，y为相对坐标。

"""

import tkinter as tk

root = tk.Tk()
tk.Label(root, text="按键").pack()


def callback(event):
    print("EventType=", event.type)
    print("keysym=", event.keysym)


frame = tk.Frame(root, bg="khaki", width=100, height=80)
frame.pack()
root.bind("<KeyPress-a>", callback)  # a 键
root.bind("<KeyPress-F1>", callback)  # F1 键
root.bind("<Control-Alt-a>", callback)  # Ctrl + Alt + a 键

root.mainloop()
