""" 继承式

上面已经说过了，通过继承不能改变控件的表现行为，但是继承式的写法，仍然会让代码更简洁，逻辑更清晰，在其他的面向对象的GUI库中，这是一种常用的写法。

"""

import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.set_window()
        self.create_top()
        self.input = tk.StringVar()
        self.create_body()
        self.create_bottom()

    # 设置窗口
    def set_window(self):
        self.title("测试")
        self.resizable(False, False)

    # 创建顶部
    def create_top(self):
        tk.Label(self, text="Top").pack()

    # 创建主体
    def create_body(self):
        tk.Entry(self, textvariable=self.input).pack()

    # 创建底部
    def create_bottom(self):
        tk.Button(self, text="Bottom", command=self.onclick).pack()

    # 按钮回调函数
    def onclick(self):
        print(self.input.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()
