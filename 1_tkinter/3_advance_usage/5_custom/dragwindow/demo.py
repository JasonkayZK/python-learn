import tkinter as tk

from drag_window import DragWindow

# 导入DragWindow类
root = DragWindow()
root.set_window_size(200, 200)
root.set_display_position(500, 400)
tk.Button(root, text="Exit", command=root.quit).pack(side=tk.BOTTOM)

root.mainloop()
