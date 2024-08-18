"""

expand和fill属性有什么区别？

两个属性是明显不同的:

- expand对应的正是要求但未使用的空间
- 而fill对应的是要求并已使用的空间。fill是填满的意思，将所有要求的空间占满。

"""

import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)

tk.Label(frame, text="Pack 布局的 side 和 fill").pack()
tk.Button(frame, text="A").pack(side=tk.LEFT, fill=tk.Y)
tk.Button(frame, text="B").pack(side=tk.TOP, fill=tk.X)
tk.Button(frame, text="C").pack(side=tk.RIGHT, fill=tk.NONE)
tk.Button(frame, text="D").pack(side=tk.TOP, fill=tk.BOTH)

# 需注意，顶部框架不会展开，也不会填充X或Y方向
frame.pack()

tk.Label(root, text="Pack 布局的 expand").pack()
tk.Button(root, text="我不扩展").pack()
tk.Button(root, text="我不向x方向填充，但我扩展").pack(expand=1)
tk.Button(root, text="我向x方向填充，并且扩展").pack(fill=tk.X, expand=1)

root.mainloop()
