""" 聚合式

通常在Python中写Tkinter界面程序时，很多人会使用这种聚合式的写法，

实际上这并不是真正纯粹的面向对象的GUI写法，但tkinter本身也仅仅是对过程式的tcl库的封装，

继承小控件并不能真正去重写控件的表现行为，因此是否继承也显得无关紧要，

但是在类似Qt这种库中则不然。

"""

import tkinter as tk


class App:
    def __init__(self, r):
        self.root = r
        self.set_window()
        self.create_top()
        self.create_body()
        self.input = tk.StringVar()
        self.create_bottom()

    # 设置窗口
    def set_window(self):
        self.root.title("测试")
        self.root.resizable(False, False)

    # 创建顶部
    def create_top(self):
        tk.Label(self.root, text="Top").pack()

    # 创建主体
    def create_body(self):
        tk.Entry(self.root, textvariable=self.input).pack()

    # 创建底部
    def create_bottom(self):
        tk.Button(self.root, text="Bottom", command=self.onclick).pack()

    # 按钮回调函数
    def onclick(self):
        print(self.input.get())


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
