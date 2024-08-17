from tkinter import *
from PIL import Image, ImageTk

# 在Label中显示图片
root = Tk()
image = Image.open("avatar.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.pack()

# 保持对 photo 的引用，防止其被垃圾回收
root.photo = photo

root.mainloop()
