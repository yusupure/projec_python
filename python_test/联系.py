import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
            }

#创建问卷数据
for i in range(1):
    #创建问卷名称
    wjfile=open(('wjfile_'+str(i+1)+'.txt'),'w')
    #创建正确答卷文件
    zqfile=open(('zqfile_'+str(i+1)+'.txt'),'w')
    #对问卷标题进行添加
    wjfile.write('name\n\ngonghao\n\n')
    wjfile.write((''*20)+'问卷准备')
    wjfile.write('\n')
    #对正确答案问卷添加标题
    zqfile.write('答卷结果')
    zqfile.write('\n')
    #加载字典中的键值并列表化
    allchus=list(capitals.keys())
    #对加载的列表进行打乱处理
    random.shuffle(allchus)
    #正确答案及数据处理、
    for j in range(50):
        #用列表的方法把对应的值全部取出
        allzqda=capitals[allchus[j]]
        #打印所有的值出来并使用列表提取
        allwrong=list(capitals.values())
        #把所有正确的答案删除
        del allwrong[allwrong.index(allzqda)]
        #对错误的答案进行分组处理每个3个一组
        allwrong=random.sample(allwrong,3)
        #组合正确答案和错误选项
        allwgzq=allwrong+[allzqda]
        #对合成数据进行打乱操作
        random.shuffle(allwgzq)
        #对问卷问题进行排列
        wjfile.write('%s.问题是 %s?\n' % (j+1,allchus[j]))
        #加入答题选项
        for k in range(4):
            wjfile.write('%s.%s\n' % ('ABCD'[k],allwgzq[k]))
        wjfile.write('\n')
        #加入打印正确答案文件
        zqfile.write('%s.%s\n' % (j+1,'ABCD'[allwgzq.index(allzqda)]))


wjfile.close()
zqfile.close()