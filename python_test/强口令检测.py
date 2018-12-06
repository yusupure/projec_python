import re
def kljc(num):
    if len(num) <=8:
        return False
    num1=re.compile(r'\d+')
    if num1.search(num)==None:
        return False
    num2 = re.compile(r'[A-Z]+')
    if num2.search(num) == None:
        return False
    num3 = re.compile(r'[a-z]+')
    if num3.search(num) == None:
        return False
    return True


a=input()
a=kljc(a)
print(a)