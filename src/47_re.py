import re

import requests


def test_match():
    str1 = 'I study python3.8 everyday'
    str2 = '简体中文'
    str3 = '123'
    str4 = '  '

    print('='*30, 'match', '='*30)  # 从左开始向右匹配 如果右一个匹配不上就会返回None
    m1 = re.match('I', str1)
    print(m1)
    print(m1.group())

    m2 = re.match('python', str1)
    print(m2)

    m3 = re.match('I study (python)', str1)
    print(m3.group(1))
    print()

    m4 = re.match('\w', str2)  # \w: 匹配包括下划线的任何单词字符包括数字包括中文 不包括-+=
    print(m4)

    m5 = re.match('\S', str4)  # \S: 非空字符 \s是指空白，包括空格、换行、tab缩进等所有的空白
    print(m5)

    m6 = re.match('\D', str3)  # \D: 非数字
    print(m6)

    m7 = re.match('.', str4)  # . 通配符
    print(m7)

    test = re.match('.\s\w+\S+\s', str1)  # *零次或者多次 +一次或者多次
    print(test)


def test_search():
    str1 = 'I study python3.8 everyday'
    str2 = '简体中文'
    str3 = '123'
    str4 = '  '

    print('='*30, 'search', '='*30)

    s1 = re.search('python', str1)
    print(s1)

    s2 = re.search('p\S+', str1)
    print(s2)


def test_findall():
    str1 = 'I study python3.8 everyday'

    f1 = re.findall('y', str1)
    print(f1)


def test_html():
    str1 = '<div><a href="https://www.baidu.com">百度</a></div>'

    f1 = re.findall('<a.*href="(.+)".*>(.+)</a>', str1)
    print(f1)


def test_bilibili_html():
    url = 'https://www.bilibili.com/v/popular/rank/bangumi'
    header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}

    resp = requests.get(url=url,headers=header)
    print(resp.text)

    print("="*60)
    f = re.findall('<a href="(\S+)" target="_blank" class="title">(.+)</a>\s*<div class="pgc-info">(.+)</div>', resp.text)
    print(f)

    for i,item in enumerate(f):
        print(i,end=' ')
        for word in item:
            print(word,end=' ')
        print()


if __name__ == '__main__':
    # test_search()
    # test_findall()
    #test_html()
    test_bilibili_html()