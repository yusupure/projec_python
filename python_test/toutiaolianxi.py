import os
import requests
from bs4 import BeautifulSoup
from hashlib import md5
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
import re
from multiprocessing import Pool
#1.提取页面HTML进入页面获取REQUEST
def get_data_html(offset):
    data={
        'offset': offset,
        'format': 'json',
       'keyword': '街拍',
        'autoload':'true',
        'count': '20',
        'cur_tab': 3
    }
    url='https://www.toutiao.com/search_content/?'+urlencode(data)
    try:
        html=requests.get(url)
        if html.status_code==200:
            return html.text
        return None
    except RequestException:
        return None

def get_parer_url(url):
    data=json.loads(url)
    if data and 'data' in data.keys():
        for i in data.get('data'):
            yield i.get('article_url')

def get_image_html(url):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    try:
        html = requests.get(url,headers=headers)
        if html.status_code == 200:
            return html.text
        return None
    except RequestException:
        return None
def get_image_url(html,url):
    soup=BeautifulSoup(html,'lxml')
    title=soup.find_all('title')[0].get_text()
    print(title)
    imagedata=re.findall(r'gallery: JSON.parse\("(.*?)"\)',html,re.S)[0].replace('\\','')
    sub_images=json.loads(imagedata)
    if sub_images and 'sub_images' in sub_images.keys():
        image=sub_images.get('sub_images')
        imageurl=[imageurllist.get('url') for imageurllist in image ]
        for i in imageurl:download_image(i)
        for imageurl in imageurl:
            return (title,imageurl,url)
def download_image(url):
    print('图片下载中',url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    try:
        html = requests.get(url, headers=headers)
        if html.status_code == 200:
            save_image(html.content)
        return None
    except RequestException:
        return None

def save_image(html):
    filename='{0}\{1}.{2}'.format(os.getcwd(),md5(html).hexdigest(),'jpg')
    with open(filename,'wb') as f:
        f.write(html)
        f.close()

def main(offset):
    htmls=get_data_html(offset)
    for url in get_parer_url(htmls):
        html=get_image_html(url)
        title, imageurl, url=get_image_url(html,url)
        print(title,imageurl,url)
        #exit()


if __name__=='__main__':
    get_start=0
    get_end=20
    ys=[x*20 for x in range(get_start,get_end)]
    pool=Pool()
    pool.map(main,ys)