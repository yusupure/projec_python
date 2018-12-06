#import requests
import json
from yzdzqk import jiaoyandizhi
class Douban():
    def __init__(self):
        self.url='https://m.douban.com/rexxar/api/v2/subject_collection/music_chinese/items?os=ios&for_mobile=1&start={}&count=18&loc_id=0&_=0'
    def _jnsjjson(self,htmls):
        datajson=json.loads(htmls)
        datajson=datajson['subject_collection_items']
        return datajson

    def _xhdrjson(self,htmls):
        with open('json.txt','a',encoding='utf-8') as f:
            for i in htmls:
                f.write(json.dumps(i,ensure_ascii=False))
                f.write('\n')
                return(i)
    def showgo(self):
        #1.开始处理初始化的地址
        number=0
        total=2550
        while number<total+18:

            jsonhtml=self.url.format(number)
            print(jsonhtml)
        #2.开始校验地址的访问情况
            jsondata=jiaoyandizhi(jsonhtml)
        #3.json获取数据并精炼数据
            data=self._jnsjjson(jsondata)
        #4.json方法把数据导出到txt文档中
            daa=self._xhdrjson(data)
            print(daa)
            number+=18

go=Douban()
go.showgo()