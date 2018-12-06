import os
def print_keywords(dict_keywords):
    key=dict_keywords.keys()
    key=sorted(key)
    for each in key:
        print('%s%s' % (each,str(dict_keywords[each])))


def line_keywords(line,keywords):
    key_index=[]
    start=line.find(keywords)
    if start!=-1:
        key_index.append(start+1)
        start=line.find(line,start+1)
    return key_index

def file_keywords(linelist,keywords):
    filelist=open(linelist,'r')
    line=0
    dict_keywords=dict()
    for each in filelist:
        line+=1
        if keywords in each:
            key_index=line_keywords(each,keywords)
            dict_keywords[line]=key_index
    filelist.close()
    return dict_keywords


def seach_file(keywords,flag):
    filepath=os.walk(os.getcwd())
    txt_list=[]
    for each in filepath:
        for eachlist in each[2]:
            if os.path.splitext(eachlist)[1]=='.txt':
                txt_list.append(each[0]+os.sep+eachlist)
    for eachline in txt_list:
        dict_keywords=file_keywords(eachline,keywords)
        print('='*50)
        print('%s%s' % (eachline,keywords))
        if flag=='是':
              print_keywords(dict_keywords)

keywords=input()

flag=input()

seach_file(keywords,flag)


