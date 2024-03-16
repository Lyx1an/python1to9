# 爬虫常用的请求模块
import requests
import json

# 伪装自己身份，以网页访问身份正常进行获取。
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Cookie': 'kg_mid=73a993634446f5dc10f5c3311580dd1d; kg_dfid=2mSLjD1lmrIY40KDl12qjjSY; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1709467164,1709518432; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1709519403'
}

# 获取音乐列表
list_url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1709519402725&mid=73a993634446f5dc10f5c3311580dd1d&uuid=73a993634446f5dc10f5c3311580dd1d&dfid=2mSLjD1lmrIY40KDl12qjjSY&keyword=%E5%91%A8%E6%B7%B1&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=08fe3bcbcaf79a37b3824c0237a02410'
list_resp = requests.get(list_url, headers=headers)
song_list = json.loads(list_resp.text[12:-2])['data']['lists']

for i, s in enumerate(song_list):
    print(f'{i + 1}----{s.get("SongName")}----{s.get("SingerName")}----{s.get("FileHash")}')

num = input("请输入要下载第几首音乐（若需全部下载请输入all）: ")

def getinfo(num):
    # 音乐信息的url
    info_url = f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={song_list[int(num) - 1]["FileHash"]}'
    info_resp = requests.get(info_url, headers=headers)
    print(info_resp.json()['data']['play_url'])

# 调用获取音乐信息的函数
getinfo(num)
