import re
from urllib.parse import urlencode
from hashlib import md5
import os
from requests.exceptions import RequestException
import requests
import json
from bs4 import BeautifulSoup
from multiprocessing import Pool
def get_page_index(offset):#1
    data={
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
    }
    url='https://www.toutiao.com/search_content/?'+urlencode(data)
    html=requests.get(url)
    try:
        if html.status_code==200:
            return html.text
        return None
    except RequestException:
        return None

def parse_page_index(html):#3
    data=json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            #print(item)
            yield item.get('article_url')

def get_page_detail(url):#4
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    try:
        html = requests.get(url,headers=headers)
        if html.status_code==200:
            return html.text
        return None
    except RequestException:
        return None

def parse_page_detail(html,url):#5
    soup=BeautifulSoup(html,'lxml')
    title=soup.select('title')[0].get_text()
    print(title)
    images_list=re.findall('gallery: JSON.parse\("(.*?)"\)',html,re.S)[0].replace('\\','')
    data=json.loads(images_list)
    if data and 'sub_images' in data.keys():
        sub_images=data.get('sub_images')
        iamges=[item.get('url') for item in sub_images]
        for iamges in iamges:download_image(iamges)
        return {
            'title':title,
            'iamges':iamges,
            'url':url
        }
def download_image(url):#6
    print('download',url)
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    try:
        html = requests.get(url,headers=headers)
        if html.status_code==200:
           save_image(html.content)
        return None
    except RequestException:
        return None
def save_image(content):#7
    file_name='{0}\{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_name):
        with open(file_name,'wb') as f:
            f.write(content)
            f.close()

def main(offset):#2
    html=get_page_index(offset)
    for url in parse_page_index(html):
        html=get_page_detail(url)
        if html:
            result=parse_page_detail(html,url)
            print(result)
if __name__=='__main__':
    group_start=0
    group_end=20
    #main()
    groups=[x*20 for x in range(group_start,group_end+1)]
    pool=Pool()
    pool.map(main,groups)