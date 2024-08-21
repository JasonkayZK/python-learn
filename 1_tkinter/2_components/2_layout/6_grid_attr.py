"""

# grid属性设置

属性名	                                属性简析	取值	取值说明
row、column	                row为行号，column为列号，设置将组件放置于第几行第几列	取值为行、列的序号，不是行数与列数	row 和 column 的序号从0开始，但是，column的默认值是0，row的默认值是下一个编号较大的未占用行号
sticky	                    设置组件在网格中的对齐方式（前提是有额外的空间）	N、E、S、W、NW、NE、SW、SE	类似于pack布局中的锚选项
rowspan	                    组件所跨越的行数	默认值为1	取值为跨越占用的行数，而不是序号
columnspan	                组件所跨越的列数	默认值为1	取值为跨越占用的列数，而不是序号
ipadx、ipady、padx、pady	    组件的内部、外部间隔距离，与pack的该属性用法相同	同pack	同pack



# 关于sticky属性，还有一些组合用法

将小控件放置在单元格的一角:

- sticky=tk.NE 右上角
- sticky=tk.SE 右下角
- sticky=tk.SW 左下角
- sticky=tk.NW 左上角

拉伸小控件:

- sticky=tk.N+tk.S 垂直拉伸小控件，并保持水平居中，其等价于字符串值"ns"，以下同
- sticky=tk.E+tk.W 水平拉伸且持垂直居中
- sticky=tk.N+tk.E+tk.S+tk.W 水平和垂直拉伸，等价于常量tk.NSEW和字符串值nsew
- sticky=tk.N+tk.S+tk.W 将垂直拉伸并向西（左）对齐


# grid函数

函数名	                                描述
grid_slaves()	                以列表方式返回本组件的所有子组件对象。
grid_configure(option=value)	给pack布局管理器设置属性，使用属性（option）= 取值（value）方式设置
grid_propagate(boolean)	        设置为True表示父组件的几何大小由子组件决定（默认值），反之则无关。
grid_info()	                    返回pack提供的选项所对应得值。
grid_forget()	                Unpack组件，将组件隐藏并且忽略原有设置，对象依旧存在，可以用pack(option, …)，将其显示。
grid_location(x, y)	            x, y为以像素为单位的点，函数返回此点是否在单元格中，在哪个单元格中。返回单元格行列坐标，(-1, -1)表示不在其中
size()	                        返回组件所包含的单元格，揭示组件大小。

"""

import tkinter as tk

parent = tk.Tk()
parent.title("Find & Replace")

tk.Label(parent, text="Find:").grid(row=0, column=0, sticky="e")
tk.Entry(parent, width=60).grid(
    row=0, column=1, padx=2, pady=2, sticky="we", columnspan=9
)

tk.Label(parent, text="Replace:").grid(row=1, column=0, sticky="e")
tk.Entry(parent).grid(row=1, column=1, padx=2, pady=2, sticky="we", columnspan=9)

tk.Button(parent, text="Find").grid(row=0, column=10, sticky="e" + "w", padx=2, pady=2)
tk.Button(parent, text="Find All").grid(row=1, column=10, sticky="e" + "w", padx=2)
tk.Button(parent, text="Replace").grid(row=2, column=10, sticky="e" + "w", padx=2)
tk.Button(parent, text="Replace All").grid(row=3, column=10, sticky="e" + "w", padx=2)

tk.Checkbutton(parent, text="Match whole word only ").grid(
    row=2, column=1, columnspan=4, sticky="w"
)
tk.Checkbutton(parent, text="Match Case").grid(
    row=3, column=1, columnspan=4, sticky="w"
)
tk.Checkbutton(parent, text="Wrap around").grid(
    row=4, column=1, columnspan=4, sticky="w"
)

tk.Label(parent, text="Direction:").grid(row=2, column=6, sticky="w")
tk.Radiobutton(parent, text="Up", value=1).grid(
    row=3, column=6, columnspan=6, sticky="w"
)
tk.Radiobutton(parent, text="Down", value=2).grid(
    row=3, column=7, columnspan=2, sticky="e"
)

parent.mainloop()
