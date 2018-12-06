import os
def print_keywords(dict_keywords):
    keys=dict_keywords.keys()
    keys=sorted(keys)
    for each in keys:
        print ('%s%s' % (each,str(dict_keywords[each])))


def line_keywords(line,keywords):
    key_index=[]
    start=line.find(keywords)
    while start!=-1:
        key_index.append(start+1)
        start=line.find(keywords,start+1)
    return key_index

def file_keywords(filename,keywords):
    f=open(filename,'r')
    line=0
    dict_keywords=dict()
    for eachline in f:
        line+=1
        if keywords in eachline:
            key_index=line_keywords(eachline,keywords)
            dict_keywords[line]=key_index
    f.close()
    return dict_keywords

def file_seach(keywords,flag):
    file=os.walk(os.getcwd())
    txt_list=[]
    for each in file:
        for eachline in each[2]:
            if os.path.splitext(eachline)[1]=='.txt':
                txt_list.append(os.path.join(each[0],eachline))
    for txt_list_path in txt_list:
        dict_keywords=file_keywords(txt_list_path,keywords)
        print('================================')
        print('%s%s' % (txt_list_path,keywords))
        if flag=='是':
            print_keywords(dict_keywords)
            
keywords=input()
flag=input()
file_seach(keywords,flag)        
