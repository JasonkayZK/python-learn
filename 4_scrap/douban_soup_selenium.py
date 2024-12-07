import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_comment():
    lst = []
    comment_elements = driver.find_elements(By.CSS_SELECTOR, "span.short")
    for com in comment_elements:
        lst.append(com.text + "\n")
    return lst


def main():
    global driver

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 可根据需要选择是否添加，比如设置为无头模式（无浏览器界面显示）
    options.add_argument("lang=zh_CN.UTF-8")  # 设置中文
    options.add_argument("disable-infobars")  # 隐藏"Chrome正在受到自动软件的控制"
    options.add_argument("--disable-gpu")  # 谷歌文档提到需要加上这个属性来规避bug

    # 创建Chrome浏览器驱动实例
    driver = webdriver.Chrome(options=options)
    f = open("流浪地球豆瓣评论.txt", "w", encoding="utf-8")
    for page in range(10):
        url = (
            "https://movie.douban.com/subject/26266893/comments?start="
            + str(20 * page)
            + "&limit=20&sort=new_score&status=P"
        )
        print("正在爬取第%s页的评论：" % (page + 1))
        print(url + "\n")
        driver.get(url)
        time.sleep(2)  # 等待页面加载完成，可根据实际情况调整等待时间
        for i in get_comment():
            f.write(i)
    print("爬取完成")
    driver.quit()  # 关闭浏览器驱动


if __name__ == "__main__":
    main()
