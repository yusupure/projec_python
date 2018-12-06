#!/usr/bin/python3
import random
import pprint

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
# 创建3张试卷(也可以创建更多)
for i in range(3):

    # 创建一个测验试卷文件
    quizFile = open('quiz%s.txt' % (i + 1), 'w')
    # 创建一个试卷答案文件
    answerFile = open('quiz_answer%s.txt' % (i + 1), 'w')
    # 给测验试卷加个头部（如让考生写姓名学号的位置，以及写分数的位置）
    quizFile.write('Name:\n\n Date:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz(Form %s)' % (i + 1))
    quizFile.write('\n\n')
    # 给答案文件加个头
    answerFile.write(' ' * 20 + 'Answer(Form %s)' % (i + 1))
    answerFile.write('\n\n')
    states = list(capitals.keys())  # 取出所有州
    # 打乱
    #random.shuffle(states)

    # 创建答案选项
    for j in range(50):
        #
        correctAnswer = capitals[states[1]]  # 正确答案
        print(correctAnswer,end='\n')
        #wrongAnswers = list(capitals.values())  # 获取所有答案列表
        #print([wrongAnswers.index(correctAnswer)])
        #del wrongAnswers[wrongAnswers.index(correctAnswer)]  # 删除正确的答案

        #wrongAnswers = random.sample(wrongAnswers, 3)  # 随机选取三个错误答案
        #answersOptions = wrongAnswers + [correctAnswer]  # 将正确答案和错误答案连接起来
        #random.shuffle(answersOptions)  # 打乱四个答案的顺序

        # 问题
        #quizFile.write('%s.What is the capital of %s?\n' % (j + 1, states[j]))
        # 答案
        #for i in range(4):
         #   quizFile.write(' %s. %s\n' % ('ABCD'[i], answersOptions[i]))
        #quizFile.write('\n')

        # 将正确答案写入一个文件

       # answerFile.write('%s. %s\n' % (j + 1, 'ABCD'[answersOptions.index(correctAnswer)]))

    quizFile.close()  # 关闭测试文件
    answerFile.close()  # 关闭答案文件