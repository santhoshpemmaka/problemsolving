def multi_of_five(l):
    res = []
    for i in l:
        # convert the "1001" to the decimal using intp = int(i,2)
        intp = int(i,2)
        if intp % 5==0:
            res.append(intp)
    print(res)

l = list(map(str,input().split()))
multi_of_five(l)
