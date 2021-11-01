import requests
import socket
import socks

if __name__ == '__main__':
    baidu_url = 'https://www.baidu.com/'
    login_page_url = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
    bili_url = 'https://www.bilibili.com/'
    google = 'http://www.google.com'
    ip = 'http://ifconfig.me/ip'
    pixiv = 'https://www.pixiv.net'

    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }

    # PAC下使用全局代理不用
    proxies = {'http': 'http://127.0.0.1:1080',
               'https': 'https://127.0.0.1:1080'}

    print('link start')
    resp = requests.get(url=login_page_url,headers=head)
    print(resp.status_code)
    print(resp.text)
