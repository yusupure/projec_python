import requests
import json
from requests.cookies import RequestsCookieJar
from zhihulogin import zhihu_cookies
from lxml import etree
from pyquery import PyQuery as pq
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

def zhihu_cookies_name():#调用登录的COOKIES
    rjar=RequestsCookieJar()
    with open("zhihucookies.json",'r') as f:
        cookies=json.load(f)
    for cookie in cookies:
        rjar.set(cookie["name"],cookie["value"])
    return rjar


def test_login_zhihu():#确认COOKIES是否有效期内，若无效则调用zhihulogin更新cookies
    url='https://www.zhihu.com/settings/account'
    html=requests.get(url,headers=headers,cookies=zhihu_cookies_name())
    if html.status_code!=200:
        zhihu_cookies()#更新cookies
    else:
        return '登录成功'

def zhihu_home_list():
    url='https://www.zhihu.com'
    html=requests.get(url,headers=headers,cookies=zhihu_cookies_name()).text
    doc=pq(html)
    all_url=doc(".ContentItem-title a")
    print(all_url.attr.href)
def main():
    if '登录成功'in test_login_zhihu():
        print('登录成功')
        print('开始处理页面数据')
        zhihu_home_list()
    else:
        return test_login_zhihu()#返回在进行测试直到成功登录


if __name__ == '__main__':
    main()