from itertools import permutations

num = int(input())
for x in range(num):
    ll=[]
    string = input()
    ss = permutations(string)
    for i in ss:
        ll.append("".join(i))
    ll.sort()
    for pp in ll:
        print(pp,end=" ")   
    print()
