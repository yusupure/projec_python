import requests
import json
from hashlib import md5
import os
import re
from requests.exceptions import RequestException
from multiprocessing import Pool
from urllib.parse import urlencode
from bs4 import BeautifulSoup
def get_page_html(offset):
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

def get_image_url(url):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    try:
        html=requests.get(url,headers=headers)
        if html.status_code==200:
            return html.text
        return None
    except RequestException:
        return None

def get_image_html(html,url):
    soup=BeautifulSoup(html,'lxml')
    title=soup.select('title')[0].get_text()
    print(title)
    imagelist=re.findall(r'gallery: JSON.parse\("(.*?)"\)',html,re.S)[0].replace('\\','')
    sub_images=json.loads(imagelist)
    if sub_images and 'sub_images' in sub_images.keys():
        image=sub_images.get('sub_images')
        imagelist=[imagenew.get('url') for imagenew in image]
        for imagelist in imagelist:download_image_url(imagelist)
        return {
                'title':title,
                'image':imagelist,
                'url':url
        }

def download_image_url(url):
    print('图片下载中',url)
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    try:
        html=requests.get(url,headers=headers)
        if html.status_code==200:
            save_image(html.content)
        return None
    except RequestException:
        return None

def save_image(html):
    file_name='{0}\{1}.{2}'.format(os.getcwd(),md5(html).hexdigest(),'jpg')
    with open(file_name,'wb') as f:
        f.write(html)
        f.close()

def main(offset):
    html=get_page_html(offset)
    for url in get_parer_url(html):
        html=get_image_url(url)
        get_image_html(html,url)


if __name__ == '__main__':
    #main()
    go_start=0
    go_end=20
    grouplist=[x*20 for x in range(go_start,go_end+1) ]
    pool=Pool()
    pool.map(main,grouplist)