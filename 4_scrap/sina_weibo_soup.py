import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


class WeiboTop(object):
    def __init__(self):
        self.url = "https://s.weibo.com/top/summary"  # 微博热搜地址

    def analysis(self):
        """提取数据"""
        results = []
        htmls = requests.get(self.url).text
        soup = BeautifulSoup(htmls, "lxml")
        ranks = soup.find_all("td", class_="td-01 ranktop")
        tags = soup.find_all("td", class_="td-02")
        hots = soup.find_all("td", class_="td-03")
        for rank, tag, hot in zip(ranks, tags, hots):
            results.append(
                [
                    rank.string if rank else "",
                    tag.a.string,
                    tag.span.string if tag.span else 9999999,
                    hot.i.string if hot.i else "",
                ]
            )
        return results

    def __sort(self):
        """排序(倒序)"""
        result = self.analysis()
        return sorted(result, key=lambda x: int(x[2]), reverse=False)  # 反向排序

    def show(self):
        """展示数据"""
        tb = PrettyTable()
        sorts_data = self.__sort()
        tb.field_names = "排名,热点话题,阅读数,热点类型".split(",")
        for i in sorts_data:
            tb.add_row(i)
        print(tb)


if __name__ == "__main__":
    wt = WeiboTop()
    wt.show()
