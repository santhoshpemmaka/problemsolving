#code
def LongestCommon(num):
    
    res = []
    num.sort()
    found=0
    for i in num[0]:
        for j in num[len(num)-1]:
            if j in num[0]:
                res.append(j)
            else:
                break
            found =1
        if found==1:
            break
    if len(res)>=1:        
        return "".join(res)
    else:
        return -1
        

num = int(input())
for i in range(num):
    number = int(input())
    l = list(map(str,input().split()))
    print(LongestCommon(l))
    
