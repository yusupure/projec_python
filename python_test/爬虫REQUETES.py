import requests
import re
from retrying import retry
requests.session()
class Shuquge():
    url='http://www.qushuge.com/novel/tunshixingkong/'
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    title='<h1>(.*?)</h1>'
    data='<div class="card mt20">(.*?)</div>'
    linke='<a href="(.*?)"'
    def __hqhtml(self):
        html=requests.get(Shuquge.url,headers=Shuquge.headers)
        htmls=html.content.decode()
        return htmls
    def __hqsj(self,htmls):
        htmlsnew=re.findall(Shuquge.data,htmls,re.S)
        #htmlstitle=re.findall(Shuquge.title,htmls)
        for i in htmlsnew:
            #typelist=re.findall(Shuquge.linke,i,re.I)
            print(i)

    def startgo(self):
        html=self.__hqhtml()
        htmls=self.__hqsj(html)
        #print(htmls)

go=Shuquge()
go.startgo()