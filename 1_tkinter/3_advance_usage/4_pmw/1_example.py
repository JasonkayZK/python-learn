from tkinter import *

import Pmw

root = Tk()
root.geometry("300x300")

lab = Label(root, text="别点我")
lab.pack()

balloon = Pmw.Balloon(root)
balloon.bind(lab, "指你妹啊")

root.mainloop()
