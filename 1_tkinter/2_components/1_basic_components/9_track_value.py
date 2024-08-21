"""

为了响应特定小控件的值的变化

Tkinter提供了自己的变量类，它们可以用来跟踪这些小控件的值。

"""

import threading
import time
import tkinter as tk

root = tk.Tk()

# 字符串型
my_string = tk.StringVar()
# 布尔型
ticked_yes = tk.BooleanVar()
# 整型
group_choice = tk.StringVar()
# 浮点型
volume = tk.DoubleVar()


def print_val():
    while True:
        print(
            "my_string: {}, ticked_yes: {}, group_choice: {}, volume: {}".format(
                my_string.get(), ticked_yes.get(), group_choice.get(), volume.get()
            )
        )
        time.sleep(1)


# 将变量类与控件关联
tk.Entry(root, textvariable=my_string).pack()
tk.Checkbutton(root, text="选我", variable=ticked_yes).pack()
tk.Radiobutton(root, text="点我", variable=group_choice).pack()
tk.Scale(root, label="音量", variable=volume).pack()

threading.Thread(target=print_val).start()

root.mainloop()
