from lxml import etree
import requests


# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple lxml
def get_bangummi_rank():
    name_xpath = '//div[@class="info"]/a/text()'
    play_num_xpath = '//span[@class="data-box" and position()=1]/text()'
    dm_num_xpath = '//span[@class="data-box" and position()=1]/text()'
    love_num_xpath = '//span[@class="data-box" and position()=1]/text()'

    url = 'https://www.bilibili.com/v/popular/rank/bangumi'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}

    resp = requests.get(url=url, headers=header)
    e = etree.HTML(resp.text)

    names = e.xpath(name_xpath)
    play_num = e.xpath(play_num_xpath)
    dm_num = e.xpath(dm_num_xpath)
    love_num = e.xpath(love_num_xpath)

    for name, play, dm, love in zip(names, play_num, dm_num, love_num):
        print(f'{name}:{play}播放{dm}弹幕{love}喜爱')


if __name__ == "__main__":
    get_bangummi_rank()
