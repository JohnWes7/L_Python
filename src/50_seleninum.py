from urllib import request
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from lxml import etree
import json
import os


cookie_path = './cookies.json'
tutu_data_path = './tutu_list.json'

pixiv_discovery_api1 = 'https://www.pixiv.net/rpc/recommender.php?type=illust&sample_illusts=auto&num_recommendations=60&page=discovery&mode=all'
pixiv_discovery_api2 = 'https://www.pixiv.net/ajax/discovery/artworks?mode=all&limit=20&lang=zh'
custom_cookie = {
    'tag_view_ranking': "RTJMXD26Ak~RcahSSzeRf~jH0uD88V6F~zyKU3Q5L4C~pzzjRSV6ZO~Bd2L9ZBE8q~Ie2c51_4Sp~bopfpc8En6~XDEWeW9f9i~D0nMcn6oGk~Lt-oEicbBr~eVxus64GZU~LJo91uBPz4~7WfWkHyQ76~q303ip6Ui5~QYelAhYfEH~1HSjrqSB3U~Dd2BFtvC_a~BtXd1-LPRH~KN7uxuR89w~aVmLrbYnSr~K8esoIs2eW~-LSsLGmCIU~gVfGX_rH_Y~skx_-I2o4Y~8Q8mLCEW16~tgP8r-gOe_~qUVF3aasqv~PzEXgc_S56~Wka710VIT8~qnGN-oHRQo~D26FCUKCS8~nuuOi_zFTA~ePN3h1AXKX~lQdVtncC-e~X_1kwTzaXt~9V46Zz_N_N~rOnsP2Q5UN~xVHdz2j0kF~cFXtS-flQO~EUwzYuPRbU~2QXu36FK5_~SW0bXgRvYs~lXvRdAunvV~57UnBqevnT~aKhT3n4RHZ~HfqELC_-Q3~Z4hQZu-rU-~_EOd7bsGyl~ziiAzr_h04~_sjpLQz14H~qmix1djJUJ~-StjcwdYwv~jk9IzfjZ6n~QaiOjmwQnI~BSlt10mdnm~gatroTOnfX~MhieHQxNXo~zdx7NJPPfr~y7byyDCjIW~CBKuoUuA6J"
}

config = {
    'image_quality': 'regular',  # thumb_mini small regular original
    'is_cover': False
}


def is_done():
    judge = input('是否完成')
    return True if judge.__eq__('yes') else False


def get_json_data(path: str):
    data = None
    if os.path.exists(path):
        with open(path, 'r') as file:
            data = json.loads(file.read())

    return data


def save_json_data(path: str, json_str: str):
    with open(cookie_path, 'w') as file:
        file.write(json_str)


def open_driver_save_cookie():
    pixiv = 'https://www.pixiv.net/'
    pixiv_login_page = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
    discover_page = 'https://www.pixiv.net/discovery'

    driver = None
    if os.path.exists('./chromedriver.exe'):
        driver = webdriver.Chrome()
    elif os.path.exists('./geckodriver.exe'):
        driver = webdriver.Firefox()

    # 打开登录页面
    driver.get(pixiv_login_page)

    #
    WebDriverWait(driver=driver, timeout=10000).until(
        expected_conditions.title_is('pixiv'))

    # 跳转到发现页面
    driver.get(discover_page)

    WebDriverWait(driver=driver, timeout=10000).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, '_2RNjBox')))

    # 获得cookie并打印
    cookies = driver.get_cookies()

    # 关闭浏览器
    driver.quit()

    # 保存cookie
    save_json_data(path=cookie_path, json_str=json.dumps(cookies))


def get_head_with_cookie():
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'referer': 'https://www.pixiv.net/discovery'
    }

    cookiejson = get_json_data(cookie_path)
    for name in custom_cookie.keys():
        tempdict = {}
        tempdict['name'] = name
        tempdict['value'] = custom_cookie.get(name)

        cookiejson.append(tempdict)

    cookiestr = ''
    for i, item in enumerate(cookiejson):
        name = item.get('name')
        value = item.get('value')
        temp = None
        if i == 0:
            temp = f'{name}={value}'
        else:
            temp = f'; {name}={value}'
        cookiestr += temp

    head['cookie'] = cookiestr

    return head


def get_link_json(head):

    str_param = {
        'type': 'illust',
        'sample_illusts': 'auto',
        'num_recommendations': '1000',
        'page': 'discovery',
        'mode': 'all'
    }

    para_str = urlencode(str_param)

    head['referer'] = 'https://www.pixiv.net/discovery'

    # 代理
    proxies = {'http': 'http://127.0.0.1:1080',
               'https': 'https://127.0.0.1:1080'}
    prox = request.ProxyHandler(proxies=proxies)

    # opener
    opener = request.build_opener(prox)

    # request
    requ = request.Request(pixiv_discovery_api2, headers=head, method='GET')

    # open
    resp = opener.open(requ)
    print(resp.getcode())
    r_bt = resp.read()
    r_str = r_bt.decode('unicode_escape')
    resp_json = json.loads(r_str)

    return resp_json


def download(id_list: list, head):

    # 代理
    proxies = {'http': 'http://127.0.0.1:1080',
               'https': 'https://127.0.0.1:1080'}
    prox = request.ProxyHandler(proxies=proxies)

    # opener
    opener = request.build_opener(prox)

    pid = 70224331
    url = f'https://www.pixiv.net/ajax/illust/{pid}/pages?lang=zh'
    head['referer'] = f'https://www.pixiv.net/artworks/{pid}'

    # 抓取图片信息
    # 包含名字和作者 simple:どちらが好きですか？ by 倉科ゆづき
    description_xpath = '//head/meta[@property="twitter:description"]/@content'
    requ_info = request.Request(
        f'https://www.pixiv.net/artworks/{pid}', headers=head, method='GET')
    info_resp = opener.open(requ_info)
    html_str = info_resp.read().decode()
    e = etree.HTML(html_str)
    tu_description = e.xpath(description_xpath)

    # 抓取图片源
    requ = request.Request(url=url, headers=head, method='GET')

    resp = opener.open(requ)
    re_byte = resp.read()
    re_str = re_byte.decode('utf-8')

    # 要抓取的图片质量
    image_quality = config.get('image_quality')
    if image_quality == None:
        image_quality = 'original'

    # 遍历获得的图片源数据
    temp_data = json.loads(re_str)
    body = temp_data.get('body')
    # 下载每一个数据源
    for i, item in enumerate(body):
        # 获得下载链接
        tu_url = item.get('urls').get(image_quality)
        suffix = os.path.splitext(tu_url)[1]
        head['referer'] = 'https://www.pixiv.net/'

        # 生成文件名
        filename = f'{pid}_{tu_description}_p{i}{suffix}'

        print(f'准备下载{filename}')

        if os.path.exists(f'./{filename}'):
            print(f'文件{filename}已经下载过了', end='')
            is_cover = False if config.get(
                'is_cover') == None else config.get('is_cover')
            if is_cover:
                print(f'正在重新下载_is_cover: {is_cover}')
            else:
                print(f'跳过_is_cover: {is_cover}')
                continue

        # 下载
        ortu_resp = opener.open(request.Request(
            url=tu_url, headers=head, method='GET'))
        # 保存
        with open(f'./{filename}', 'wb') as file:
            file.write(ortu_resp.read())


def parsing_tutu_data2(jsondata):
    id_list = []

    re_list = jsondata.get('body').get('recommendedIllusts')
    for item in re_list:
        id_list.append(item.get('illustId'))

    return id_list


if __name__ == '__main__':
    open_driver_save_cookie()
    tutu_data = get_json_data(tutu_data_path)

    id_list = parsing_tutu_data2(tutu_data)

    head = get_head_with_cookie()

    download(id_list=id_list, head=head)
