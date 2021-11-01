import requests
import os
from config import config


def test():
    url = 'https://www.bilibili.com/'
    agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}

    # 注意记得看时post还是get
    response1 = requests.get(url=url, headers=agent)
    response2 = requests.get(url=url)

    print(response1.text)
    print("="*40)
    print(response2.text)


def get_text_of_url(url: str, agent=None):
    response = requests.get(url=url, headers=agent)

    print(response.text)


def work1():
    anima_url = 'https://www.bilibili.com/v/douga'
    # anima_url = 'https://www.bilibili.com/'
    agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}

    
    get_text_of_url(url=anima_url,agent=agent)
    print()
    print('='*100)
    print()
    get_text_of_url(url=anima_url)

def print_animation_rank_from_bilibili():
    rank_url = 'https://api.bilibili.com/pgc/web/rank/list?season_type=1&day=3'
    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}

    print(f'从{rank_url}开始获取数据')
    response = requests.get(url=rank_url,headers=header)
    json = response.json()
    print('成功获得json')
    print(json)
    
    # 保存json到本地
    # with open(config.absolute_create_files_PATH + '/bili_anime_rank_json.json','w', encoding='utf-8') as file:
    #     file.write(response.text)

    result = json.get('result')
    note = result.get('note')
    print('='*len(note))
    print(note)

    for item in result.get('list'):
        rank = item.get('rank')
        title = item.get('title')
        rating = item.get('rating')
        new = item.get('new_ep').get('index_show')

        print(f'{rank}:{title}', end='\t')
        print('暂无评分', end='\t') if rating.__eq__('') else print(f'评分:{rating} ', end='\t')
        print(new)


if __name__ == "__main__":
    print_animation_rank_from_bilibili()

    
