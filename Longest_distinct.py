def Longest_character(string):
    count =0
    for i in range(len(string)):
        str = ""
        for j in range(i,len(string)):
            if string[j] not in str:
                str+=string[j]
            else:
                break
        count = max(count,len(str))
    return count
    
n = int(input())
for i in range(n):
    s = input()
    print(Longest_character(s))

"""
Input:-
Input:
2
abababcdefababcdab
geeksforgeeks

Output:
6
7
"""
