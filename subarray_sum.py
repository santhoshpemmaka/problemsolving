#code
"""
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Ouput:
2 4
1 5

Explanation : 
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15
"""
def Subarraysum(arr,number):
    found =0
    for i in range(len(arr)):
        sum1=0
        res = []
        for j in range(i,len(arr)):
            sum1 = sum1+arr[j]
            if sum1 <= number:
                res.append(j+1)
            if sum1 == number:
                return res
    return -1   
n = int(input())
for t in range(n):
    num,num1 = map(int,input().split())
    l = list(map(int,input().split()))
    result = Subarraysum(l,num1)
    if result == -1:
        print(result)
    else:
        print(result[0],result[-1])

    

    

