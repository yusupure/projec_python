from random import shuffle,sample
class pkp():
    def __init__(self):
        huase=['黑桃','葵扇','红心','菱角']
        shuzi=['A','J','Q','K',2,3,4,5,6,7,8,9,10]
        self.decklist=[f'{each}{eachnum}'for each in huase for eachnum in shuzi]
        self.count=52
    def __repr__(self):
        return (f'{self.play1}\n{self.play2}\n{self.play3}]\n{self.play4}')
    def shufflea(self):
        shuffle(self.decklist)
    def autopkp(self):
        self.play1=self.decklist[:13]
        self.play2=self.decklist[13:26]
        self.play3=self.decklist[26:39]
        self.play4=self.decklist[39:52]
        return (self.play1,self.play2,self.play3,self.play4)
c=pkp()
c.shufflea()
c.autopkp()
print(c)