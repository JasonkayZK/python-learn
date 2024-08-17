from tkinter import *

root = Tk()

Label(root, text="这是一个标签").pack()
Button(root, text="按钮").pack()
Checkbutton(root, text="多选框").pack()
Entry(root).pack()
Radiobutton(root, text="男", value=1).pack()
Radiobutton(root, text="女", value=2).pack()
Scale(root, orient='horizontal').pack()

root.mainloop()
