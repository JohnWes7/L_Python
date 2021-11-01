import requests
import os
import time


def get_vedio_imgs():
    search_url = 'https://api.bilibili.com/x/space/arc/search?mid=17832078&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}

    print(f'正在获取{search_url}')
    respone = requests.get(url=search_url, headers=header)
    print('数据获取成功')

    json = respone.json()
    vlist = json.get('data').get('list').get('vlist')

    for v in vlist:
        pic_url = v.get("pic")
        title = v.get('title')
        title = str(title).replace('/','／')

        print(f'正在下载图片{title} from {pic_url}')
        pic_resp = requests.get(url=pic_url, headers=header)

        temp = os.path.splitext(pic_url)
        suffix = temp[len(temp) - 1]
        path = f'/c_pics/{title}{suffix}'
        with open(path,'wb') as file:
            file.write(pic_resp.content)

        print('下载成功')
        pic_resp.close()

def save_NanaNatsu_imgs():
    docs_url = 'https://api.bilibili.com/x/dynamic/feed/draw/doc_list?uid=1803155766&page_num=0&page_size=30&biz=all&jsonp=jsonp'
    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}

    print(f'正在获取{docs_url}')
    resp = requests.get(url=docs_url,headers=header)
    items = resp.json().get('data').get('items')
    print('获取成功')
    
    for item in items:
        ct = item.get('ctime')
        pictures = item.get('pictures')
        title = str(item.get('title')).replace('/','／')
        str_time = time.ctime(ct)

        for img in pictures:
            img_src = img.get("img_src")
            temp = os.path.splitext(img_src)
            suffix = temp[len(temp) - 1]
            
            print(f'下载{img_src}')
            img_resp = requests.get(url=img_src,headers=header)

            path = f'/{title}{suffix}'

            with open(path,'wb') as file:
                file.write(img_resp.content)
            
            print('下载完成')
            img_resp.close()
            
    
    print('下载成功')
    resp.close()


if __name__ == '__main__':
    # get_vedio_imgs()
    save_NanaNatsu_imgs()
    input("done")
    pass