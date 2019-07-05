#code
"""
Input:
2
4
2 1 4 3 1 2 3 2 3 6 2 3 5 2 5 3
5
12 1 14 3 16 14 2 1 3 35 14 1 14 3 11 14 25 3 2 1 1 18 3 21 14

Output:
2
3
"""
def distinct(num):
    
    for i in num:
        res =i
        break
    res = set(res)
    l = []
    for i in range(1,len(num)):
        r = set(num[i])
        l.append(list(res.intersection(r)))
    min1 =999
    for i in l:
        min1 = min(len(i),min1)
    print(min1)
        
num = int(input())
for i in range(num):
    number = int(input())
    l1=[]
    l = list(map(int,input().split()))
    for i in range(0,len(l),number):
        l1.append(l[i:i+number])
    distinct(l1)
