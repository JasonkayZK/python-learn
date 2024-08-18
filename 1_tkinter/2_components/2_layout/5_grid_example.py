"""

要注意，每列的宽度（或每行的高度）由网格中小部件的高度或宽度决定。

如果需要额外的设置，只能通过设置网格中的小部件的宽度实现。

另外，可以使用sticky = tk.NSEW参数使小部件可扩展并填充网格的整个单元格。


在tkinter的官方文档中，并没有给出让grid布局适配根窗口拉伸的方法，但是通过查阅tcl/Tk的文档，可知设置权重能满足该需求。

"""

import tkinter as tk

root = tk.Tk()
tk.Label(root, text="账号").grid(row=0, sticky=tk.W)
tk.Label(root, text="密码").grid(row=1, sticky=tk.W)
tk.Entry(root).grid(row=0, column=1, sticky=tk.E)
tk.Entry(root, show='*').grid(row=1, column=1, sticky=tk.E)
tk.Button(root, text="Login").grid(row=2, column=1, sticky=tk.E)
root.mainloop()
