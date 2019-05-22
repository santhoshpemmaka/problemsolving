#code
num = int(input())
for i in range(0,num):
    number = int(input())
    l = list(map(int,input().split()))
    sum1 =0
    max_sum =0
    for i in range(0,number):
        max_sum= max_sum+l[i]
        if max_sum > sum1:
            sum1 = max_sum
        if max_sum < 0:
            max_sum =0
    if (sum1 == 0):
        print(l[0])
    else:
        print(sum1)
            
        
