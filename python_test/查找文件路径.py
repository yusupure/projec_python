import os  
def search_file(search_dir, obj_file):  
    os.chdir(search_dir)  
  
    for each_file in os.listdir(search_dir):  
        if obj_file == each_file:  
            print(os.path.join(search_dir,obj_file))  
  
        elif os.path.isdir(each_file):  
            cur_dir = os.path.join(search_dir,each_file) # 当前搜索目录  
            search_file(cur_dir, obj_file) # 递归调用  
            os.chdir(os.pardir) # 递归调用后返回上一层目录           
if __name__=='__main__':
    search_dir = input("请输入待查找的初始目录:")
    obj_file = input("请输入需要查中安的目标文件:")
    search_file(search_dir, obj_file)
