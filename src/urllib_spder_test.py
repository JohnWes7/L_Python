from http import cookiejar
from urllib import request
import json
import re
from http.cookiejar import CookieJar, MozillaCookieJar
from urllib.parse import urlencode
import webbrowser


def pixiv():
    pixiv = 'https://www.pixiv.net/'
    pixiv_discovery_api = 'https://www.pixiv.net/rpc/recommender.php?type=illust&sample_illusts=auto&num_recommendations=1000&page=discovery&mode=all'

    pixiv_login_api = 'https://accounts.pixiv.net/api/login?lang=zh'
    pixiv_login_page = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'

    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }

    # 暴力从浏览器上直接复制下来
    head_cookie = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': "first_visit_datetime_pc=2021-10-21+21:35:08; p_ab_id=2; p_ab_id_2=2; p_ab_d_id=14195249; yuid_b=IEYhInk; _gcl_au=1.1.1717990878.1634819714; __utmz=235335808.1634819715.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.1005042063.1634819715; device_token=ec00b1fdd744e5ed9453690287bf437c; c_type=25; privacy_policy_notification=0; a_type=0; b_type=1; ki_r=; ki_s=214908:0.0.0.0.2;214994:0.0.0.0.2;215190:0.0.0.0.2;219376:0.0.0.0.0; login_ever=yes; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=25832134=1^9=p_ab_id=2=1^10=p_ab_id_2=2=1^11=lang=zh=1; stacc_mode=unify; _im_vid=01FJPDR8PWHT2Z3ANY0HNNBY13; privacy_policy_agreement=3; __utmc=235335808; _gid=GA1.2.191364372.1635145130; tag_view_ranking=RcahSSzeRf~9vxLUp1ZIl~9Nx-lbSnZF~q303ip6Ui5~KN7uxuR89w~gVfGX_rH_Y~X_1kwTzaXt~Lt-oEicbBr~RTJMXD26Ak~EUwzYuPRbU~CER84-k5HW~1HSjrqSB3U~FeEqwTOACZ~1Si6FEFSPh~3jgr4pevko; categorized_tags=IVwLyT8B6k~RcahSSzeRf; tags_sended=1; _im_uid.3929=b.ceff9bd4f3a16ce6; ki_t=1634985399331;1635145141119;1635151414645;2;14; __cf_bm=cM9FyJetX3iR.uQ_N92LcPs0dRVC9.ggadmzAihLYks-1635154981-0-ARwH8unB6Q6XWtAQQoVS+986V7FMEvb7FaDW4b7FXxLRechv6AkCLi5YBEal8tKh+YeAlb55LV+g+n6ADFd6TP67s0hZcuox0A9OKrL6CKHC+0dST0jcALxbHeaAIXxlHQaSSVPaH9RBi/jl9aO6QdOROY7Akv3MtNEvi08f5TZlx3Owzc+TT/3p6Y+J/xNZzw==; __utma=235335808.1005042063.1634819715.1635149109.1635154984.11; __utmt=1; PHPSESSID=25832134_DHTeLdwPXqeGckC1IrzgxFYlRAI5r4du; __utmb=235335808.5.10.1635154984",
        'referer': 'https://www.pixiv.net/discovery'
    }

    proxies = {'http': 'http://127.0.0.1:1080',
               'https': 'https://127.0.0.1:1080'}

    # urllib
    # 设置代理
    prox = request.ProxyHandler(proxies)

    # cookie对象这一种方式不用手动保存cookie，后期直接调用同一个opener即可，因为cookie已经在opener对象中
    cookie = CookieJar()
    # 创建handler
    cookie_handlder = request.HTTPCookieProcessor(cookiejar=cookie)

    # 创建opener
    opener = request.build_opener(prox,cookie_handlder)
    # 创建request
    reqe = request.Request(url=pixiv_login_page,headers=head, method='GET')

    #打开postkey页面
    resp = opener.open(reqe)
    print(resp.getcode())
    url_bytes = resp.read()

    # 得到登录页面的postkey
    url_text = url_bytes.decode('utf-8')
    # print(url_text,'\n\n\n')
    postkey = re.search(',"pixivAccount.postKey":"(\w*)",', url_text)
    print(postkey.group(1))

    #发送登录请求
    data = {
        'password':'lyj2001417',
        'pixiv_id':'1246215651@qq.com',
        'post_key':postkey.group(1),
        'source':'pc',
        'return_to':'https://www.pixiv.net/',
        'recaptcha_enterprise_score_token':'03AGdBq24Jfkk3T98e1XsHzW3oRrtzMHsZmlZ7dmqvEqGP1JhBa_9AGaCAt6UgcQwu_Hwuggsrf0jG5zerui1c13AaIjmZ0ioPbmEA1dagqd5cP3os5SriO6QK9xRJqSaEWycJTVEp38lNUHMV5W-oWDGIGaoKsmuDxKfayhxa-Zd3qJ6trjWEtFB8a__8V25x_CT5VjsqoCpyOJJmAJWys11LbhEVwHvdcl1uIoRJSEd4P8LWaUn0dQltpaAXn7AB3YksIAw9_f37lYcMUWJsQrO5ZyGYJohwX2wkXDfbKSJzT3Fuqb0cTuUR9Rbh0EKpv8__ky6zJ1XuR3RNrbe-YVfqqAvaLV9D3SdbCltmlqbsyXWl6KyeV_Lz11MRfwch7mHgjG-uEKZqMob5KtrArdbmMGNfNCEaPDWYsCuFRs6GJhy91H6wEJJY5UQQ7rpm9J2Qp5WbLVlY5mjmcK7B1X95ca9FH16Cl9qTYSI5aBtk_WQw5V91QTvpyxf6cIu-U-akA98ZdnzqwBsAPmM8Nrxr1eju7oqqB25EFs6qwH_dj3qEDO07eFjWdz6ayQGaF5RkxVLHIAaoV85y-h93uurn0UErOhw_vw5zcyHO9-QZra_ZzUC12bDcn-GGmD6mDtpLgWIyIB-3lNwcufcPZvXn1vLZEr3uKraTngw8d_a5bZHnBBgGvIzDWRFQJFzBlGEadyrr-ttI4VHayaEx4tXCz6ZO6gnxJdiCWatpyzZ6-77jkXpss3sQ1Gw79XNvObaft2AvITZsAvgfiAmfofWBkRPIc5VbOGCg2PUSoPFwHmH3ZSeUj1jObBWaXOXQyXx1euAnmVkXCPICwabpeCuHA3EOPkl8czKvBjanOASN3WIE4MeIvaRdsG8Y-RKm1OtNa3h38Km2mW7UhVmvKo-YL0zxelSPj67s_rMiWfEZogtEXUXZdOKcvO478Q87qgw5Sbu2xGwMYi-qBYr2ENgbJWrr4IlRDo0ulLc37olmVUGf3qPZ_F6euM_jOfPkCYGWoDoX8SpI3y2jilBZfj6bGedXr6MoSmj3qcNxU58uGRRgIYh9taq7WkjmoIPSqLxXk7dmbYxX_Mgz08BfJW9v0MiPSpCTFIQ8Zt3YrWRoEIWSrhtNgGGrGjg2ETpMDbQYFVr6d2RRA8IdkjMwVdabZ3mimrqbr4YEnRGHWh9Kok-Cw4qSVv1IA6-G4zhkOeECFBP2Ertx96OynIx2rh7mnPC1IbU0rlEcXDRiOyU10kUvttieyEld4jnjHOLc7HGWZT6t6iRU46M5jwSpc0ncJ7O9wTKvQKxZm6-RSJIupElyuN_JmMfMZfUTeWu8TfoSMhLSx5JKeM6bshncKNzyAHVjj4lWLylqOSlAVDJNRAEpMj0-KvHLlwhfafiHRnCvevCEEFmggtAFQ1H0OdifnnRQcFa9a337idBN3HYoLYEfHoY-edTs5pv4KxAw6Kq_KdCAHc_cUS89be7JwFsFc5zRRue2CN4RTBJrPHveW9KWPFkhqbD9DFPNtbz-d2-XHIOJbGE0AXgAow7Jt0CY5-krLsuUFrzQrmugLzmwCwxtz6i0HcL8-ezu0_Y2La6U8BozLttv1x6YTF4k4BGIBtakn6XU0wyFy3x3NDAExvp7K622MQrz5dX8MWIXyJzRuEuONvVnjeIeEi-YOilomrMSrt9iIbkEKG0AgkCzzxhA-hdBnRkD6m5MzwJEqAociC3BapcjwVV6h6PMHAx_Ib-5qjVVrteDfpeX52dqhqopnUo-W2bXAzJHenk-TMWrJTK-pGUR0uS9IX1qA5tjjFF--iWZhQ',
        'tt':'ad6e3619e347e3c8c35293e2ee99ba29'
    }
    login_api_response = opener.open(request.Request(url=pixiv_login_api, headers=head, method='POST'), data=urlencode(data).encode())
    print(login_api_response.getcode())
    login_b = login_api_response.read()
    print(login_b)
    login_text = login_b.decode('unicode_escape')
    print(login_text)


def test():
    bili_url = 'https://www.bilibili.com'
    baidu = 'https://www.baidu.com/'
    google = 'https://www.google.com/'
    pixiv = 'https://www.pixiv.net/'
    rank = 'https://api.bilibili.com/pgc/web/rank/list?season_type=1&day=3'

    pixiv_discovery = 'https://www.pixiv.net/rpc/recommender.php?type=illust&sample_illusts=auto&num_recommendations=1000&page=discovery&mode=all'

    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }

    resp2 = request.urlopen(request.Request(url=rank, headers=head, method='GET'))
    json_str = resp2.read().decode('utf-8')

    rank_data = json.loads(json_str)
    rank_list = rank_data.get('result').get('list')
    for item in rank_list:
        print(item.get('title'))


def test2():
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }

    pixiv = 'https://www.pixiv.net/'

    proxies = {'http': 'http://127.0.0.1:1080',
               'https': 'https://127.0.0.1:1080'}

    # urllib
    # 设置代理
    prox = request.ProxyHandler(proxies)

    # cookie对象这一种方式不用手动保存cookie，后期直接调用同一个opener即可，因为cookie已经在opener对象中
    cookie = CookieJar()
    # 创建handler
    cookie_handlder = request.HTTPCookieProcessor(cookiejar=cookie)

    # 创建opener
    # opener = request.build_opener(prox,cookie_handlder)
    
    # r = opener.open(request.Request(url=pixiv, headers=head, method='GET'))
    # r_text = r.read().decode()

    # print(r_text)

    webbrowser.open(pixiv)

def not_login():
    pixiv = 'https://www.pixiv.net/'
    pixiv_discovery_api = 'https://www.pixiv.net/rpc/recommender.php?type=illust&sample_illusts=auto&num_recommendations=1000&page=discovery&mode=all'

    pixiv_login_api = 'https://accounts.pixiv.net/api/login?lang=zh'
    pixiv_login_page = 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'

    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }

    # 暴力从浏览器上直接复制下来
    head_cookie = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        #'cookie': "first_visit_datetime_pc=2021-10-21+21:35:08; p_ab_id=2; p_ab_id_2=2; p_ab_d_id=14195249; yuid_b=IEYhInk; _gcl_au=1.1.1717990878.1634819714; __utmz=235335808.1634819715.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.1005042063.1634819715; device_token=ec00b1fdd744e5ed9453690287bf437c; c_type=25; privacy_policy_notification=0; a_type=0; b_type=1; ki_r=; ki_s=214908:0.0.0.0.2;214994:0.0.0.0.2;215190:0.0.0.0.2;219376:0.0.0.0.0; login_ever=yes; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=25832134=1^9=p_ab_id=2=1^10=p_ab_id_2=2=1^11=lang=zh=1; stacc_mode=unify; _im_vid=01FJPDR8PWHT2Z3ANY0HNNBY13; privacy_policy_agreement=3; __utmc=235335808; _gid=GA1.2.191364372.1635145130; tag_view_ranking=RcahSSzeRf~9vxLUp1ZIl~9Nx-lbSnZF~q303ip6Ui5~KN7uxuR89w~gVfGX_rH_Y~X_1kwTzaXt~Lt-oEicbBr~RTJMXD26Ak~EUwzYuPRbU~CER84-k5HW~1HSjrqSB3U~FeEqwTOACZ~1Si6FEFSPh~3jgr4pevko; categorized_tags=IVwLyT8B6k~RcahSSzeRf; tags_sended=1; _im_uid.3929=b.ceff9bd4f3a16ce6; ki_t=1634985399331;1635145141119;1635151414645;2;14; __cf_bm=cM9FyJetX3iR.uQ_N92LcPs0dRVC9.ggadmzAihLYks-1635154981-0-ARwH8unB6Q6XWtAQQoVS+986V7FMEvb7FaDW4b7FXxLRechv6AkCLi5YBEal8tKh+YeAlb55LV+g+n6ADFd6TP67s0hZcuox0A9OKrL6CKHC+0dST0jcALxbHeaAIXxlHQaSSVPaH9RBi/jl9aO6QdOROY7Akv3MtNEvi08f5TZlx3Owzc+TT/3p6Y+J/xNZzw==; __utma=235335808.1005042063.1634819715.1635149109.1635154984.11; __utmt=1; PHPSESSID=25832134_DHTeLdwPXqeGckC1IrzgxFYlRAI5r4du; __utmb=235335808.5.10.1635154984",
        'referer': 'https://www.pixiv.net/discovery'
    }

    proxies = {'http': 'http://127.0.0.1:1080',
               'https': 'https://127.0.0.1:1080'}

    # urllib
    # 设置代理
    prox = request.ProxyHandler(proxies)
    # cookie对象这一种方式不用手动保存cookie，后期直接调用同一个opener即可，因为cookie已经在opener对象中

    # opener
    opener = request.build_opener(prox)
    reqe = request.Request(url=pixiv_discovery_api,
                           headers=head_cookie, method='GET')
    resp = opener.open(reqe)
    print(resp.getcode())
    url_bytes = resp.read()
    print(url_bytes)

    print('\n\n\n', '='*100, '\n\n')

    url_text = url_bytes.decode('utf-8')
    print(url_text)


if __name__ == '__main__':
    # test2()
    # test()
    # pixiv()
    not_login()
