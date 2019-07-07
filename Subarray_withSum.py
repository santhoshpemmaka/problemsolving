#code
def subarray_sum(arr,n):
    r = []
    for i in range(len(arr)):
        
        sum1 =0
        for j in range(i,len(arr)):
            
            if sum1<n:
                sum1 = sum1+arr[j]
            if sum1 > n:
                break
            if sum1 == n:
                r.append(i+1)
                r.append(j+1)
                return r
    return False
    
    
num = int(input())
for i in range(num):
    num1,num2 = map(int,input().split())
    l = list(map(int,input().split()))
    r =subarray_sum(l,num2)
    if r:
        print(r[0],r[1])
    else:
        print(-1)
"""
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5
"""
