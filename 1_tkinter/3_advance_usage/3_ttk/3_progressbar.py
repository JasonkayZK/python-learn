""" Progressbar

进度条控件

Progressbar 参数说明：

mode: 有两个值可选。

- "indeterminate"表示来回反弹样式
- "determinate"表示步进样式

"""

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
ttk.Label(root, text="编程语言").pack(side=tk.LEFT, padx=5, pady=5)

combo = ttk.Combobox(root, values=["Go", "Python", "Java", "C++"])
# 设置当前选中的项
combo.current(1)
combo.pack(side=tk.LEFT, padx=5, pady=5)

# 创建进度条控件
progress = ttk.Progressbar(root, mode="indeterminate", length=100)
progress.pack(pady=10, padx=10)

# 启动进度条控件
progress.start()

progress2 = ttk.Progressbar(root, mode="determinate", length=100)
progress2.pack(pady=10, padx=10)
progress2.start()

root.mainloop()
