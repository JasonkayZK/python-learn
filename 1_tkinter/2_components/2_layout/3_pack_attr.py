""" pack常用属性

属性名	                属性简析	取值	取值说明
fill	        设置组件是否向水平或垂直方向填充	X、Y、BOTH 和NONE	fill = X（水平方向填充）fill = Y（垂直方向填充）fill = BOTH（水平和垂直）NONE 不填充
expand	        设置组件是否展开，当值为YES时，side选项无效。组件显示在父容器中心位置；若fill选项为BOTH,则填充父组件的剩余空间。默认为不展开	YES 、NO（1、0）	expand=YES expand=NO
side	        设置组件的对齐方式	LEFT、TOP、RIGHT、BOTTOM	值为左、上、右、下
ipadx、ipady	设置x方向（或者y方向）内部间隙（子组件之间的间隔）	可设置数值，默认是0	非负整数，单位为像素
padx、pady	    设置x方向（或者y方向）外部间隙（与之并列的组件之间的间隔）	可设置数值，默认是0	非负整数，单位为像素
anchor	        锚选项，当可用空间大于所需求的尺寸时，决定组件被放置于容器的何处	N、E、S、W、NW、NE、SW、SE、CENTER（默认值为CENTER）	表示八个方向以及中心

注意：

- 上表中取值都是常量，YES等价于"yes"，亦可以直接传入字符串值。
- 另外当界面复杂度增加时，要实现某种布局效果，需要分层来实现。

pack函数

函数名	                                描述
pack_slaves()	                以列表方式返回本组件的所有子组件对象。
pack_configure(option=value)	给pack布局管理器设置属性，使用属性（option）= 取值（value）方式设置
propagate(boolean)	            设置为True表示父组件的几何大小由子组件决定（默认值），反之则无关。
pack_info()	                    返回pack提供的选项所对应得值。
pack_forget()	                Unpack组件，将组件隐藏并且忽略原有设置，对象依旧存在，可以用pack(option, …)，将其显示。
location(x, y)	                x, y为以像素为单位的点，函数返回此点是否在单元格中，在哪个单元格中。返回单元格行列坐标，(-1, -1)表示不在其中
size()	                        返回组件所包含的单元格，揭示组件大小。

"""

from tkinter import *

root = Tk()

# 使用Frame增加一层容器
fm1 = Frame(root)

Button(fm1, text="Top").pack(side=TOP, anchor=W, fill=X, expand=YES)
Button(fm1, text="Center").pack(side=TOP, anchor=W, fill=X, expand=YES)
Button(fm1, text="Bottom").pack(side=TOP, anchor=W, fill=X, expand=YES)
fm1.pack(side=LEFT, fill=BOTH, expand=YES)

fm2 = Frame(root)
Button(fm2, text="Left").pack(side=LEFT)
Button(fm2, text="This is the Center button").pack(side=LEFT)
Button(fm2, text="Right").pack(side=LEFT)
fm2.pack(side=LEFT, padx=10)

root.mainloop()
