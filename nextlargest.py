#code
"""
Input
2
4
1 3 2 4
4
4 3 2 1
Output
3 4 4 -1
-1 -1 -1 -1
"""
def nextlarger(arr):
    num= len(arr)
    l = []
    for i in range(num):
        max1=0
        for j in range(i+1,num):
            if arr[i] < arr[j]:
                max1 = arr[j]
                l.append(max1)
                break
        if max1 ==0:
            l.append(-1)
    for i in l:
        print(i,end=" ")
    print()
num = int(input())
for i in range(num):
    num1 = int(input())
    l = list(map(int,input().split()))
    nextlarger(l)
            
        
            
