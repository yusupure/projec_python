import easygui as g

msg="注册账户"
title="登记信息"
filename=("*用户名","*密码","地址","*电话","*手机")
filevalues=[]
filevalues=g.multenterbox(msg,title,filename)

while True:
    if filevalues==None:
        break
    errmsg=""
    for i in range(len(filename)):
        opt=filename[i].strip()
        if filevalues[i].strip()=="" and opt[0]=="*":
            errmsg+=('%s' % filename[i])
    if errmsg=="":
        break
    filevalues = g.multenterbox(errmsg, title, filename,filevalues)
print(str(filevalues))