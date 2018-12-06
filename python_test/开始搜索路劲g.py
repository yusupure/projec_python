import os  
def print_keywords(dict_keywords):  
    keys = dict_keywords.keys()  
    keys = sorted(keys)  
    for each in keys:  
        print('关键字出现在第 %s 行，第 %s 个位置。'  
              % (each, str(dict_keywords[each])))  
      
def line_keywords(line, keywords):  
    key_index = []  
    start = line.find(keywords)  
    while start!=-1:  
        key_index.append(start+1)  
        start = line.find(keywords, start+1)  
    return key_index         
      
  
def file_keywords(filename, keywords):  
    f = open(filename,'r')  
    line = 0  
    dict_keywords = dict()  
    for each_line in f:  
        line +=1  
        if keywords in each_line:  
                key_index = line_keywords(each_line, keywords)  
                dict_keywords[line]= key_index  
    f.close()  
    return dict_keywords  
  
      
def file_search(keywords, flag):  
    all_files = os.walk(os.getcwd())  
    txt_list = []  
  
    for each in all_files:
        for filename in each[2]:
            if os.path.splitext(filename)[1]== '.txt':  
                txt_list.append(os.path.join(each[0],filename))  
  
    for each_txt_file in txt_list:
        dict_keywors = file_keywords(each_txt_file, keywords)  
        print('====================================================')  
        print('在文件【%s】中找到关键字【%s】' % (each_txt_file, keywords))  
  
        if flag in ['YES', 'Yes', 'yes']:  
              print_keywords(dict_keywors)  
          
keywords = input("请将该脚本放于待查找的文件夹中，请输入关键字:")  
flag = input("请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）:")  
file_search(keywords, flag)  
