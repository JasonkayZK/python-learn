""" Entry

Entry 一个单行文本输入框。可以用来接受用户的输入，但是只能输入一行。
如果你只是想显示而不是编辑，那么应该使用标签。

w = Entry(parent, option=value ... )

需要注意一点，Entry与 Label 和 Button 不同，其text属性是无效的。
那么需要让Entry显示文字该如果操作呢？

方法	描述
delete ( first, last=None )	删除字符的部件，在指标之一，但不包括在最后位置的字符开始。如果第二个参数被忽略，只有在单个字符的位置被删除.
get()	返回当前组件的字符串
icursor ( index )	在给定索引处的字符之前插入光标
index ( index )	移动entry的内容，使得给定索引处的字符是最左边的可见字符。 如果文本在entry中刚好完全显示，则不起作用。
insert ( index, s )	将字符串s插入给定索引处的字符之前。
select_adjust ( index )	此方法用于确保选中的部分包含指定索引处的字符。
select_clear()	清除选中的。 如果当前没有选中的，则不起作用。
select_from ( index )	将ANCHOR索引位置设置为由索引选择的字符位置，并选择该字符。
select_present()	如果有选择，则返回true，否则返回false。
select_range ( start, end )	在程序控制下设置选择。 选择从开始索引处开始的文本，但不包括结束索引处的字符。 起始位置必须在结束位置之前。
select_to ( index )	选择从ANCHOR位置开始的所有文本，但不包括给定索引处的字符。
xview ( index )	此方法在将Entry链接到水平滚动条时非常有用。
xview_scroll ( number, what )	用于水平滚动Entry。 参数必须是UNITS，按字符宽度滚动，或者按页面大小来滚动。 数字是从左到右滚动的正数，负数从右到左滚动。
"""

from tkinter import *

root = Tk()
e = StringVar()
# 使用textvariable属性，绑定字符串型跟踪变量e
entry = Entry(root, textvariable=e)
e.set("请输入……")
entry.pack()

passwd = Entry(root, show="*")
passwd.pack()
root.mainloop()
