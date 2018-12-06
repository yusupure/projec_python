from urllib import request
import requests
import re

class Htmls():
    url='https://www.panda.tv/cate/lol'
    jqsj='<div class="video-info">([\d\D]*?)</div>'
    zhmc='</i>([\d\D]*?)</span>'
    renqi='<span class="video-number">([\d\D]*?)</span>'
    def __searchdata(self):#获取HTML的数据信息
        r=request.urlopen(Htmls.url)
        htmls=r.read()
        htmls=str(htmls,encoding='utf-8')
        return htmls
    def __sjhq(self,htmls):#获取特定数据，中间进行筛选，正则表达式(提取需要数据方式
        htmlsd=re.findall(Htmls.jqsj,htmls)
        typelist=[]
        for i in htmlsd:
            name=re.findall(Htmls.zhmc,i)
            number=re.findall(Htmls.renqi,i)
            typedict={'name':name,'number':number}
            typelist.append(typedict)
        return typelist
    def __jlsj(self,htmls):#精炼数据
        l=lambda htmls:{'name':htmls['name'][0].strip(),
                        'number': htmls['number'][0].strip()
                        }
        return map(l,htmls)
    def __sord(self,htmls):#排序

        htmls=sorted(htmls,key=self.__sord_next,reverse=True)
        #print(htmls)
        #return htmls

    def __sord_next(self,dict_new):
        #print(dict_new)
        r=re.findall('\d*',dict_new['number'])
        number=float(r[0])
        if '万'in dict_new['number']:
            number*=10000
            print(number)
        return number

        #lista=[]
        #for i in htmls:
            #tylist={'name':i['name'][0].strip(),'number':i['number'][0].strip()}
            #lista.append(tylist)
        #return lista
    #def __show(self,htmls):
        #for i in range(0,len(htmls)):
            #print('rank '+str(i+1)+'   '+htmls[i]['name']+'    '+htmls[i]['number'])
    def go(self):
        urldata=self.__searchdata()
        htmlsd = self.__sjhq(urldata)
        htmlsd=list(self.__jlsj(htmlsd))
        htmlsd = self.__sord(htmlsd)
        #htmlsd = self.__show(htmlsd)



a=Htmls()
a.go()