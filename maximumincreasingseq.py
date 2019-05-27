       
num = int(input())
for k in range(0,num):
    number = int(input())
    arr = list(map(int,input().split()))
    res = []
    res = arr
    """Check for the condition arr[i] > arr[j] and 
        res[i] < res[j]+arr[i]
    """    
    for i in range(1,number):
        for j in range(0,i):
            if (arr[i] > arr[j] and res[i] < (res[j]+arr[i])):
                res[i] = res[j]+arr[i]
                print(res[i],end=" ")    
    maximum_sum =0
    for i in res:
        maximum_sum = max(i,maximum_sum)
    print(maximum_sum)
    
