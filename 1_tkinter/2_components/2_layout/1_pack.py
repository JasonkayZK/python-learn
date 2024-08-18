""" Pack

pack 布局
使用 pack布局，将向容器中添加组件，第一个添加的组件在最上方，然后是依次向下添加。
当pack布局不设置属性时，它只会占用能容纳下当前组件的最小空间

pack布局区分以下三种空间

- 所属不明的，无人认领的空间
- 要求但未使用的空间
- 要求并已使用的空间

"""

import tkinter as tk

root = tk.Tk()

# 展开属性expand
tk.Button(root, text="A").pack(side=tk.LEFT, expand=1)
tk.Button(root, text="B").pack(side=tk.LEFT, expand=1)
tk.Button(root, text="C").pack(side=tk.LEFT, expand=1)

root.mainloop()
