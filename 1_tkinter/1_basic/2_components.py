import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="我是一个标签")
button = tk.Button(root, text="我是一个按钮")

label.pack()
button.pack()

root.mainloop()
