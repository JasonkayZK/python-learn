""" Text

Text控件是非常灵活复杂的控件，既可以插入文字，还能插入图片和其他小控件
我们没有必要一次掌握它的全部用法，这里介绍一下基本用法

# Text的索引

其索引表示比较复杂，有常量，也有字符串，常用的有如下:

- INSERT 等价于字符串"insert"，表示当前光标的位置
- CURRENT 等价于字符串"current"，当前鼠标所在的位置
- END 等价于字符串"end"，表示文本最末的位置
- line.column 直接指定行列位置，如"1.0"，表示第一行第一列，注意，行号从1开始，列号从0开始。
- line.end 指定行末位置，如"1.end"，表示第一行结尾的位置

不常用的:

- + n chars 如"1.0+5c"，表示在第一行第一列的位置向右移动五个字符的位置
- linestart 如"current linestart"，表示当前光标所在行的行首位置

"""

from tkinter import *

from PIL import Image, ImageTk

content = "汉皇重色思倾国，御宇多年求不得。杨家有女初长成，养在深闺人未识。" "天生丽质难自弃，一朝选在君王侧。回眸一笑百媚生，六宫粉黛无颜色。"


def touch(_event):
    print(text_area.index(CURRENT))
    print(text_area.get(CURRENT, END))


# 清空Text
def clear():
    text_area.delete("1.0", END)


root = Tk()

# 创建垂直滚动条
y_bar = Scrollbar(root, orient=VERTICAL)
y_bar.pack(side=RIGHT, fill=Y)

text_area = Text(root, yscrollcommand=y_bar.set, wrap=WORD)
y_bar["command"] = text_area.yview

text_area.bind("<Motion>", touch)
text_area.pack()

# 插入文本内容
text_area.insert(INSERT, content)
text_area.insert("1.0", "这是一句XXX话")

# 插入图片
image = Image.open("avatar.jpg")
photo = ImageTk.PhotoImage(image)
text_area.image_create(END, image=photo)

# 插入控件
btn = Button(text_area, text="点我", command=clear)
text_area.window_create(END, window=btn)

root.mainloop()
