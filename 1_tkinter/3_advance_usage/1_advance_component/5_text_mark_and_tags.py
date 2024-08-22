""" Mark与Tags的简单用法

Mark主要用来控制位置，Tags主要用来改变内容的样式

"""

from tkinter import *

content = "汉皇重色思倾国，御宇多年求不得。杨家有女初长成，养在深闺人未识。" "天生丽质难自弃，一朝选在君王侧。回眸一笑百媚生，六宫粉黛无颜色。"

root = Tk()

text_area = Text(root, wrap=WORD)
text_area.pack()

# 插入文本内容
text_area.insert(INSERT, content)

# 创建一个mark
text_area.mark_set("xxx", "1.0")

# 在名为"xxx"的mark处插入文本，第三参数为插入的文本设置一个名为"here_red"的tag
text_area.insert("xxx", "这是一句XXX话", "here_red")

# 设置Tag的样式
text_area.tag_config("here_red", foreground="red")

# 解除mark
text_area.mark_unset("xxx")

# 在指定范围创建一个tag
text_area.tag_add("high_light", "1.50", "1.end")
text_area.tag_config("high_light", background="yellow")

# 在全局删除指定的tag
# text_area.tag_delete("here_red")
# 在指定的范围内删除tag
# text_area.tag_remove("here_red", "1.0", "1.end")

root.mainloop()
