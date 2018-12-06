import os
filepath=os.listdir(os.curdir)
typedict=dict()
typedict2=dict()
for each in filepath:
    if os.path.isdir(each):
        typedict.setdefault('文件夹',0)
        typedict['文件夹']+=1
    else:
        ext=os.path.splitext(each)[1]
        typedict.setdefault(ext,0)
        typedict[ext]+=1

for eachdata in typedict.keys():
    print(eachdata,typedict[eachdata])


for eachsize in filepath:
    filesize=os.path.getsize(eachsize)
    typedict2.setdefault(eachsize,filesize)

for eachdata in typedict2.items():
    print(eachdata[0],eachdata[1])
