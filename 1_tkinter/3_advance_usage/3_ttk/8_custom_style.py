""" 样式与控件状态样式的定制

在ttk中，控件实际上是一个字符串，要改变控件样式，需要指定这个字符串名称，而不是类名

它们的对应关系如下

类名	                    控件样式名
Button	            TButton
Checkbutton	        TCheckbutton
Combobox	        TCombobox
Entry	            TEntry
Frame	            TFrame
Label	            TLabel
LabelFrame	        TLabelFrame
Menubutton	        TMenubutton
Notebook	        TNotebook
PanedWindow	        TPanedwindow
Progressbar	        Horizontal.TProgressbar或Vertical.TProgressbar
Radiobutton	        TRadiobutton
Scale	            Horizontal.TScale 或 Vertical.TScale
Scrollbar	        Horizontal.TScrollbar 或Vertical.TScrollbar
Separator	        TSeparator
Sizegrip	        TSizegrip
Treeview	        Treeview

需要注意，在创建新样式时，应当定义newName.oldName形式的名称

"""

from tkinter import Tk, ttk

root = Tk()

style = ttk.Style()

# 定义一个全局样式作为默认样式（"."表示此样式将应用于顶级窗口及其所有子元素）
style.configure(".", font="Arial 14", foreground="brown", background="yellow")

# 未指定样式时，使用全局默认样式
ttk.Label(root, text="我没有指定样式").pack()

# 定义一个名为danger的新样式（newName.oldName格式）
style.configure("danger.TButton", font="Times 12", foreground="red", padding=1)
ttk.Button(root, text="我使用danger样式", style="danger.TButton").pack()

# 为小控件的不同状态指定样式
style.map(
    "new_state_style.TButton", foreground=[("pressed", "red"), ("active", "blue")]
)
ttk.Button(text="不同状态不同样式", style="new_state_style.TButton").pack()

# 覆盖Entry的当前主题（即使没有指定样式，也会受到主题更改的影响）
current_theme = style.theme_use()
style.theme_settings(
    current_theme,
    {
        "TEntry": {
            "configure": {"padding": 10},
            "map": {"foreground": [("focus", "red")]},
        }
    },
)

ttk.Entry().pack()

root.mainloop()
