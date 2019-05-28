
def first_ele(arr,num1):
    num = len(arr)
    count_map = {}
    for i in range(num):
        if arr[i] in count_map.keys():
            count_map[arr[i]]+=1
        else:
            count_map[arr[i]]=1
    for i in range(num):
        if count_map[arr[i]] == num1:
            return arr[i]
    return -1
    
n = int(input())
for i in range(0,n):
    num,num1 = map(int,input().split())
    l = list(map(int,input().split()))
    print(first_ele(l,num1))
"""
 arr = [1,7,4,3,4,8,7]
 
 for i in range(len(arr)):
    print(count_map[arr[i]])
    'output:- 1,2,2,1,2,1,2'
print(count_map) => {8:1,1:1,3:1,4:2,7:2}
    
    
    
