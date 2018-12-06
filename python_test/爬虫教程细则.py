#Python训练营（2018.5.30更新）AP 38
import requests as rq
#url='https://icanhazdadjoke.com'
#r=rq.get(url,headers={'Accept':'text/plain'})
#print(r.text)打印文字
#print(r.url)打印URL
#print(r.encoding)打印文字编码
#$print(r.headers)#打印标题
#print(r.status_code)#打印执行返回值
#r=rq.get(url,headers={'Accept':'text/plain'})返回页面的数据
#r=rq.get(url,headers={'Accept':'application/json'},)返回JSON值
#url='https://icanhazdadjoke.com/search'
#r=rq.get(url,headers={'Accept':'application/json'},params={'term':'son','limit':'10'})
#print(r.json(),end='\n\n') 提取JSON返回的一个字典数据
#print(r.json()['results'][0]['joke'])通过字典查询方式来查询对应的数据
#dic=r.json()转换JSON为字典
#print(dic)
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#练习JSON查询
import requests as rq
from random import choice,seed
url='https://icanhazdadjoke.com/search'
user_input=input()
while user_input!='q':
    r=rq.get(url,headers={'Accept':'application/json'},params={'term':user_input}).json()
    total=r['total_jokes']
    if total==0:
        print('没有任何资料')
    elif total==1:
        print(f'{total}')
        print(r['results'][0]['joke'])
    else:
        print(f'{total}')
        print(choice(r['results'])['joke'])
        seed()
    user_input=input()
print('88')