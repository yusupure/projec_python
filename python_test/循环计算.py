def  collatz(num):
    if num %2==0:
        num=num//2
    else:
        num=3*num+1
    return (num)
try:
    i=int(input())
    while i !=1:
        i=collatz(i)
        print(i)
except (ValueError):
    print('请勿输入字符')