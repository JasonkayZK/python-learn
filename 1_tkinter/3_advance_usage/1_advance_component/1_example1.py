"""

LabelFrame
Message
OptionMenu
Spinbox

"""

from tkinter import *

content = "汉皇重色思倾国，御宇多年求不得。杨家有女初长成，养在深闺人未识。\
            天生丽质难自弃，一朝选在君王侧。回眸一笑百媚生，六宫粉黛无颜色。"

root = Tk()
root.geometry("300x400")
top = LabelFrame(root, text="这是 Label")
top.pack(padx=8, pady=8)

# 创建一个Label
Label(top, text=content, bg="yellow").pack()

bottom = LabelFrame(root, text="这是 Message")
bottom.pack(padx=8, pady=8)

# 创建一个Message
Message(bottom, text=content, bg="blue").pack()

# 下拉菜单
op_list = ["选项1", "选项2", "选项3"]
val = StringVar()
val.set(op_list[0])
# 注意，传入的列表前需要加一个*号，这是表示不定参的传递，
# 两个*则是表示字典类型的不定参传递
OptionMenu(root, val, *op_list).pack()

# 指定数字范围
var_range = StringVar()
var_range.set("0")
Spinbox(root, textvariable=var_range, from_=-10, to=10).pack()

# 指定列表范围
Spinbox(root, values=op_list).pack()

root.mainloop()
