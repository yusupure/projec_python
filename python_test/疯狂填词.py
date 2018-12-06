import re
#打开需要替换的问题文件并进行只读操作
f=open('D:\\python3\\test.txt','r')
#读取文件内容并赋值给wenben
wenben=f.read()
f.close()
#创建关键字符串的关键子
gj=re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
#并对GJ进行匹配关键字符
th=gj.findall(wenben)
#循环进行替换处理
for w in th:
    thzf=input(f'{w}\n')
    zczf=re.compile(w)
    wenben=zczf.sub(thzf,wenben,1)

newfile=open('test2.txt','w')
newfile.write(wenben)
newfile.close()
