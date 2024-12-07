#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import re

from selenium import webdriver
from selenium.webdriver.common.by import By


def scrap_sina_toplist(options):
    try:
        # 打开网页:
        browser = webdriver.Chrome(options=options)
        browser.get(
            "https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=topindex"
        )

        # 第一位排名的序号为2, 因为新浪微博有置顶的飙升最快的事件!
        xpath_casename_left = (
            "/html/body/div[1]/div[2]/div/div[2]/div[1]/table/tbody/tr["
        )
        xpath_casename_right = "]/td[2]/a"

        # 同理, 此序号也为2开始!!!
        xpath_hotpoint_left = (
            "/html/body/div[1]/div[2]/div/div[2]/div[1]/table/tbody/tr["
        )
        xpath_hotpoint_right = "]/td[2]/span"

        # 用列表类型来整合toplist, each_info存放每一个的表单
        toplist = list()
        each_info = dict()

        # 时间戳处理:
        year = datetime.datetime.now().strftime("%Y")
        month = datetime.datetime.now().strftime("%m")
        day = datetime.datetime.now().strftime("%d")
        hour = datetime.datetime.now().strftime("%H")
        minute = datetime.datetime.now().strftime("%M")
        now_time = year + "/" + month + "/" + day + ":" + hour + ":" + minute

        for i in range(2, 22):  # 仅仅处理前20位的新闻变化, 放弃排名较靠下的新闻
            # 头条事件名处理:
            try:
                xpath_casename = xpath_casename_left + str(i) + xpath_casename_right
                each_info["name"] = browser.find_element(
                    by=By.XPATH, value=xpath_casename
                )
                # 正则表达式,去掉逗号, 并将"name"处理为str类型!:
                each_info["name"] = re.sub(",", "", each_info["name"].text)
            except Exception as e:
                print(e)
                break

            # 头条对应热度处理:
            try:
                xpath_hotpoint = xpath_hotpoint_left + str(i) + xpath_hotpoint_right
                each_info["hotpoint"] = browser.find_element(
                    value=xpath_hotpoint, by=By.XPATH
                )
            except Exception as e:
                print(e)
                break

            # 排行榜序列索引
            each_info["index"] = i - 1

            # 处理时间戳
            each_info["time"] = now_time

            # 加入处理后的数据到列表toplist中:
            toplist.append(each_info)
            each_info = dict()

        # 输出到文件中:
        # 打开文件追加a模式
        filename = ".\sina\sina_hotlist.txt"
        fileout = open(filename, "a+", encoding="utf-8")
        # 写入数据:
        for i in toplist:
            fileout.writelines(
                i["name"]
                + ","
                + str(i["index"])
                + ","
                + i["hotpoint"].text
                + ","
                + i["time"]
                + "\n"
            )

    finally:
        # 关闭文件和窗口:
        fileout.close()
        browser.close()


# -----------------------------------------  程序开始处 -------------------------------------------#

# 设置Chrome请求头(非无头模式):
options = webdriver.ChromeOptions()
options.add_argument("--headless")

options.add_argument("lang=zh_CN.UTF-8")  # 设置中文
options.add_argument("disable-infobars")  # 隐藏"Chrome正在受到自动软件的控制"
options.add_argument("--disable-gpu")  # 谷歌文档提到需要加上这个属性来规避bug
# 更换头部
user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) "
    + "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)
options.add_argument("user-agent=%s" % user_agent)

# 运行爬虫程序:
scrap_sina_toplist(options)
