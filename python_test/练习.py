def fav(**name):
    for eachname,eachvalue in name.items():
        print('%s最喜欢的颜色是%s' % (eachname,eachvalue))




name=dict(小明='蓝色',小航='绿色')
fav(**name)