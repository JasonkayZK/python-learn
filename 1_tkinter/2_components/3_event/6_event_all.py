"""

# 绑定级别

事件有三种绑定级别，实际开发中选择合适的一种即可

- 实例绑定。将事件绑定到一个特定的控件实例上。如下述代码中的鼠标事件绑定到Frame实例上：

frame.bind("<Button-1>", callback)

- 类级绑定。可以将事件绑定到类的所有窗口小控件上。

典型使用如下，所有Entry控件都将绑定到事件，该事件将调用名为paste的函数，类级绑定须慎用，以免造成不可预知的问题！

my_entry.bind_class（'Entry'，'<Control-V>'，paste）

- 应用程序级绑定。只要应用程序的任何一个窗口处于焦点，事件发生时回调函数都会被调用。

root.bind_all（'<F1>'，show_help）

只要应用程序处于焦点，按F1键将始终触发 show_help函数回调

"""

""" 取消绑定

事件被注册后，是可以取消的，三种级别绑定的取消方法如下

entry.unbind('<Alt-Shift-5>')
root.unbind_all('<F1>')
root.unbind_class('Entry', '<KeyPress-Del>')

"""

""" 手动模拟事件

有时候我们需要用代码模拟生成一个事件，发送给监听者，而不是通过操作事件源产生事件

tkinter中所有的widget都包含一个公共方法event_generate,这个方法就是用来产生相应的事件的

event_generate("<<Copy>>")

要想查看这些内置的事件，需要查看Tk/tcl的文档，tkinter只是对Tk/tcl的封装，因此tkinter的文档并不是非常全面

"""
