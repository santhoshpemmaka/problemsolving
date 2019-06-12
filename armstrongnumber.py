# Checking the armstrong number

def armstrong(num):
    n = len(num)
    result = int(num)
    sum1 = 0
    for i in range(n):
        sum1+=(int(num[i])**(n))
    if result == sum1:
        return "Yes"
    else:
        return "No"

num = int(input())
for i in range(num):
    num1 = input()
    print(armstrong(num1))
    
