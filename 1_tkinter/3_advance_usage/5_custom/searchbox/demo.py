import tkinter as tk

from search_box import SearchBox

g_list = [
    "Aaron",
    "Abbott",
    "dart",
    "Abel",
    "Abner",
    "Abraham",
    "Absalom",
    "Ace",
    "Adair",
]


# 输入回调
def callback_func(text):
    print(text)
    if not text:
        search.update(None)
        return

    tmp = []
    for it in g_list:
        if it.startswith(text):
            tmp.append(it)

    # 更新弹出框内容
    search.update(tmp)


root = tk.Tk()

tk.Label(text="搜索框").pack()

search = SearchBox(root, callback=callback_func)
search.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
