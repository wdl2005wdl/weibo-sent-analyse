
import csv
import requests
import time
 
headers = {
    'Cookie': "SCF=Al0PoUL0xMPauns7dgWwGG3wxcCWRJ0LZeWS-6rEewHN0euoF3bREcYpMoqotl0GqY1m1gfefombwTViIKmFgyM.; SUB=_2A25FME1ADeRhGeBN6lIS8CzLwj6IHXVmTMCIrDV8PUNbmtANLXTBkW9NRIFHuTd4qtwsAQsjQba2uaMYhU_t2FZW; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WheU4Mde1B9SPa4ep3nwQGQ5JpX5KzhUgL.Foq0eK50ehzN1Kz2dJLoIpMLxKnLB.qL1K.LxKqL1KnLB-q7eGU.d5tt; ALF=02_1750845968; UOR=127.0.0.1:8888,v6.bang.weibo.com,127.0.0.1:8888; SINAGLOBAL=6275870970643.358.1748254857388; ULV=1748440907507:3:3:3:846110216105.489.1748440907477:1748346174631; XSRF-TOKEN=bdiEBe-ekZuRBdNO4tTTGUk6; PC_TOKEN=aa60d25401; WBPSESS=bHRZqzqMb8txYslJVyF9-CZ5DkoEXYp6a2DHK8630icmHY5LHnTvbKMqHV_Lhe6ZI0dL2ANtRiVxeGgbZhUY_fgnKvgcP882yi2ZkDkP4durL09rdWG27ZGlVgoKHpSjg8KF-1yR77WjTjVpgDmmRQ==",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
 
}
 
url = 'https://m.weibo.cn/comments/hotflow'
f = open('spider.csv', mode='w+', encoding='utf-8', newline='')
writer = csv.writer(f)
 
 
def get(msgid):
    data = {
        'id': msgid,
        'mid': msgid,
        'max_id_type': 0,
    }
    print(type(data['id']))
    # input()
    resp = requests.get(url=url, headers=headers, params=data).json()
    max_id = resp['data']['max_id']
    mid_t = resp['data']['max_id_type']
    data_list = resp['data']['data']
    for dicts in data_list:
        
        testt = dicts['source'].replace("来自","")
        # print(testt)
        # input()

        # user_name = dicts['user']['screen_name']  # 用户名
        like_count = dicts['like_count']  # 点赞该评论数
        text = dicts['text'].split('<')[0].replace(",","z")  # 评论
        # user_url = dicts['user']['profile_url']  # 用户微博链接
        created_at = dicts['created_at']  # 评论时间
        writer.writerow([text,testt, created_at,like_count])
        # print(1)
        # time.sleep(3)  # 睡一下
        # print(2)
        # print( text + " "+ str(like_count)+" "+ testt +" "+str(created_at))
    # input()
    get2(max_id,msgid,mid_t)
 
 
def get2(max_id,msgid,mid_t):
    a = 1
    mid_t = mid_t
    while True:
        data2 = {
            'id': msgid,
            'mid': msgid,
            'max_id': max_id,
            'max_id_type': mid_t
        }
        # resp2 = requests.get(url=url, headers=headers, params=data2).json()
        resp2 = requests.get(url=url, headers=headers, params=data2).json()
        print(resp2)
        # input()
        max_id = resp2['data']['max_id']
        mid_t = resp2['data']['max_id_type']
        # print(resp2)
        data_list = resp2['data']['data']
        for dicts in data_list:
            testt = dicts['source'].replace("来自","")
            # user_name = dicts['user']['screen_name']  # 用户名
            like_count = dicts['like_count']  # 点赞该评论数
            text = dicts['text'].split('<')[0].replace(",","")  # 评论
            # user_url = dicts['user']['profile_url']  # 用户微博链接
            created_at = dicts['created_at']  # 评论时间
            writer.writerow([text,testt, created_at,like_count])
            # print( text + " "+ str(like_count)+" "+ testt +" "+str(created_at))
        if a == 100:  # 我没爬完，10页左右
            break
        if data2['max_id_type'] != 0:
            break
        a += 1
 
 
 
def main(spidermsg):
    headers['Referer'] = spidermsg
    msgid = headers['Referer'].split('detail/')[1]
    get(int(msgid))
    return "数据收集成功!"
 
 
# if __name__ == '__main__':
#     main()


'''

'''
