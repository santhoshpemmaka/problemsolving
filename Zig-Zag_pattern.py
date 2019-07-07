#code
def convert_zigzag(num):
    for i in range(len(num)):
        try:
            if i%2 ==0:
                if num[i]>num[i+1]:
                    num[i],num[i+1]=num[i+1],num[i]
            else:
                if num [i] < num[i+1]:
                    num[i],num[i+1]=num[i+1],num[i]
        except:
            flag=1
            
    for i in num:
        print(i,end=" ")
    print()
    
n = int(input())
for i in range(n):
    number = int(input())
    l = list(map(int,input().split()))
    convert_zigzag(l)
    
"""
The converted array should be in form a < b > c < d > e < f.
Input:
2
7
4 3 7 8 6 2 1
4
1 4 3 2
Output:
3 7 4 8 2 6 1
1 4 2 3
"""



