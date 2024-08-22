# 打包发布

## py文件与pyw文件

通常python中的脚本文件都是`.py`后缀格式，但如果编写的是`tkinter`的图形程序，则应当以`.pyw`格式为脚本后缀名。

`.pyw`格式与`.py`最显著的区别是，运行前者不会生成一个黑框控制台，而是直接以图形界面程序运行。具体来说，`pyw`格式有如下区别

1.  运行时不会弹出控制台窗口（DOS 窗口）
2.  所有向`stdout`和`stderr`的输出都无效
3.  所有从`stdin`的读取都只会得到`EOF`

<br/>

Reference:

-   https://www.bczl.xyz/tkinter/doc/5%20%E5%BA%94%E7%94%A8%E6%89%93%E5%8C%85.html





