# coding=utf-8
from  urllib import request
import requests
import re
# 断点调试
# class Spider():
#     url='https://www.panda.tv/cate/lol'
#     root_pattern='<div class="video-info">[\s\S]*?</div>'#?是贪婪，非贪婪，现在是非贪婪
#     def __fetch_countent(self): #打开要解析的网页
#         r=request.urlopen(Spider.url) #这里Spider.url是一个实例的意思
#         htmls= r.read()
#         htmls=str(htmls,encoding='utf-8')
#         print(htmls)
#         return htmls
#         a=1
#
#     def __analysis(self,htmls): #具体分析
#         root_html=re.findall (Spider.root_pattern,htmls)
#         print(root_html)
#         a=1
#     def go(self):
#         htmls=self.__fetch_countent()
#         self.__analysis(htmls)
#
#
# youtube=Spider()
# youtube.go()

class Spider():
    url='https://www.panda.tv/cate/lol'
    root_pattern='<div class="video-info">([\s\S]*?)</div>' #这里选取非贪婪模式
    name_pattern='</i>([\s\S]*?)</span>'
    number_patter='<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):  #取得_内容
        print('1111')
        r=requests.get(Spider.url)
        r.enconding = "utf-8"
        htmls=r.content.decode("utf-8")

        return htmls
    def __analysis(self,htmls): #分析内容
        root_html=re.findall(Spider.root_pattern,htmls) #findall 需要2个参数，一个是正则内容，一个是正则对象
        list_renqi=[]
        for html in root_html:
            name=re.findall(Spider.name_pattern,html)
            number=re.findall(Spider.number_patter,html)
            dic_renqi={'name':name,'number':number}
            list_renqi.append(dic_renqi)
        a=1
        print('111')

        return  list_renqi
    def __refine(self,list_renqi):#精炼列表
        l=lambda dic_renqi:{'name':dic_renqi['name'][0].strip(),
                            'number':dic_renqi['number'][0].strip()
                            }
        return map(l,list_renqi)

    def __sort(self,list_renqi): #排序
        list_renqi=sorted(list_renqi,key=self.__sort_seed,reverse=True) #key指定需要比较大小的元素 #reverse是排列顺序，是正序还是倒叙
        print(list_renqi)
        return list_renqi

    def __sort_seed(self,dic_renqi): #这是给上边排序函数用的，目的是找出key的方法，用来排序
        r=re.findall('\d*',dic_renqi['number'])# 这里是把‘万’子变成10000，用来排序
        number=float(r[0])
        if '万' in dic_renqi['number']:
            number *=10000
        return  number

    def __show(self,list_renqi):
        for rank in range(0,len(list_renqi)):
            print('rank '+str(rank+1)
                  +':'+list_renqi[rank]['name']
                  +'     '+list_renqi[rank]['number'])
        # for renqi in list_renqi:
        #     print(renqi['name']+'-------'+renqi['number'])

    def go(self):  #总控
        htmls=self.__fetch_content()  #获得内容
        list_renqi=self.__analysis(htmls) #分析内容
        list_renqi=list(self.__refine(list_renqi)) #精炼内容
        print(type(list_renqi))
        list_renqi=self.__sort(list_renqi)  #排序
        list_renqi=self.__show(list_renqi)  #展示
        print(list_renqi)

spider=Spider()
spider.go()