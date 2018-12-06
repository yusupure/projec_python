if __name__=='__main__':
    name=[{'姓':'刘','名':'玄德'},{'姓':'关','名':'云长'},{'姓':'张','名':'易德'}]
    data=list(map(lambda name:name.get('姓'),name))
    #print(data)


    nums=[-8,9,48,0,-5.1,-7.4]
    lt1=list(filter(lambda nums:nums>=0,nums))
    #print(lt1)


    name2=['Carter','sime','Tom','eaae']
    lt2=list(filter(lambda name2: name2.istitle(),name2))
    #print(lt2)


    name='hello'
    for s in reversed(name):
        print(s)
