import requests
from retrying import retry

headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
         'Referer':'https://m.douban.com/music/'
         }
@retry(stop_max_attempt_number=3)
def _jiaoydizhi(url):
    print('OK')
    htmls=requests.get(url,headers=headers)
    newhtmls=htmls.content.decode()
    return newhtmls
def jiaoyandizhi(url):
    try:
        datamessage=_jiaoydizhi(url)
    except:
        datamessage=None
    return datamessage