import requests
import re
class Qushuge():
    url='http://www.qushuge.com/novel/guanjia/'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    datahtml='<ul class="dirlist clearfix">(.*?)</ul>'
    htmlsdata='<a href="(.*?)" title="[\s\S]+?" target="_blank">(.*?)</a>'
    link='<a href="(.*?)"'
    def _tqhtml(self):#提取HTML
        htmls=requests.get(Qushuge.url,headers=Qushuge.headers)
        htmldata=htmls.content.decode()
        return htmldata
    def _gldata(self,htmls):#提取内容
        htmllist=re.findall(Qushuge.datahtml,htmls,re.S)
        for i in htmllist:
            linklist=re.findall(Qushuge.htmlsdata,i)

        return linklist

    def _glnr(self,htmls):
        listlink=[]
        with open('test.txt','a',encoding='utf-8') as f:
            for i in htmls:
                listlink.append('http://www.qushuge.com{}'.format(i[0]))
            for each in range(0,len(listlink)):
                htmlsnew = requests.get(listlink[each], headers=Qushuge.headers)
                htmldata = htmlsnew.content.decode()

                newdata=re.findall('<div class="content" id="chaptercontent">(.*?)</div>',htmldata,re.S)[0]
                newdata1=newdata.replace('<br/>','')
                newdata1=newdata1.strip()
                newdata1 = newdata1.replace('　　','')

                f.write(newdata1)
                f.write('\n\n')
                print('下载比例:{:.2f}%'.format(each/len(listlink)*100))




    def go(self):
        htmls=self._tqhtml()
        newhtmls=self._gldata(htmls)
        self._glnr(newhtmls)
        #print(newhtmls)


show=Qushuge()
show.go()