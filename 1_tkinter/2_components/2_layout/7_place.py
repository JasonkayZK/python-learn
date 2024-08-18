""" place布局

最简单最灵活的一种布局，使用组件坐标来放置组件的位置。

但是不太推荐使用，在不同分辨率下，界面往往有较大差异。

# place属性设置

属性名	                        属性简析	取值	取值说明
anchor	                锚选项，同pack布局	默认值为 NW	同pack布局
x、y	                组件左上角的x、y坐标	整数，默认值0	绝对位置坐标，单位像素
relx、rely	            组件相对于父容器的x、y坐标	0~1之间浮点数	相对位置，0.0表示左边缘（或上边缘），1.0表示右边缘（或下边缘）
width、height	        组件的宽度、高度	非负整数	单位像素
relwidth、relheight	    组件相对于父容器的宽度、高度	0~1之间浮点数	与relx（rely）取值相似
bordermode	            如果设置为INSIDE，组件内部的大小和位置是相对的，不包括边框；如果是OUTSIDE，组件的外部大小是相对的，包括边框	INSIDE、OUTSIDE(默认值INSIDE)	可以使用常量INSIDE、OUTSIDE，也可以使用字符串形式"inside"、"outside"


# place函数

函数名	                                    描述
place_slaves()	                以列表方式返回本组件的所有子组件对象。
place_configure(option=value)	给pack布局管理器设置属性，使用属性（option）= 取值（value）方式设置
propagate(boolean)	            设置为True表示父组件的几何大小由子组件决定（默认值），反之则无关。
place_info()	                返回pack提供的选项所对应得值。
grid_forget()	                Unpack组件，将组件隐藏并且忽略原有设置，对象依旧存在，可以用pack(option, …)，将其显示。
location(x, y)	                x, y为以像素为单位的点，函数返回此点是否在单元格中，在哪个单元格中。返回单元格行列坐标，(-1, -1)表示不在其中
size()	                        返回组件所包含的单元格，揭示组件大小。

"""

import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("Tkinter Place 示例")

# 创建标签
label1 = tk.Label(root, text="标签1", bg="lightblue")
label1.place(x=50, y=50)

# 创建按钮
button1 = tk.Button(root, text="按钮1")
button1.place(x=150, y=50)

# 创建输入框
entry1 = tk.Entry(root)
entry1.place(x=50, y=100)

# 运行主循环
root.mainloop()
