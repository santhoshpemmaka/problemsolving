#code
def Longestseq(arr):
    
    n = len(arr)
    res = [1] *n
    
    for i in range(1,n):
        for j in range(0,i):
            if arr[i]>arr[j] and res[i] < res[j]+1:
                res[i] = res[j]+1
    maximum =0
    for i in res:
        maximum = max(maximum,i)
    return maximum
    

num = int(input())
for i in range(0,num):
    number = int(input())
    l = list(map(int,input().split()))
    print(Longestseq(l))
