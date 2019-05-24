#code
num = int(input())
for i in range(num):
    number = int(input())
    l = list(map(int,input().split()))
    found =0
    l2 =[]
    # first  store first local minimum value index after that next 
    # local maximum value compare to previous value store index
    for i in range(0,number-1):
        if  found==0:
            if l[i] < l[i+1]:
                found =1
                l2.append(i)
        else:
            if l[i] > l[i+1]:
                l2.append(i)
                found =0
    if len(l2) % 2 ==1:
        num = l2[-1]
        if l[num] < l[number-1]:
            l2.append(number-1)
    else:
        l2.pop()
    for i in range(0,len(l2),2):
        print((l2[i],l2[i+1]),end='')
    print()
            
