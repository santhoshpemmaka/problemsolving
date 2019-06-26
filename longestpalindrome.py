"""

Input:
1
aaaabbaa

Output:
aabbaa

Explanation:
Testcase 1: The longest palindrome string present in the given string is "aabbaa"
"""
def Longeststring(string):
    res = []
    k =[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            res.append(string[i:j])
    print(res)
    for i in res:
        if i == i[::-1]:
            k.append(i)
    print(k)
    ll = max(k,key=len)
    print(ll)
    
num = int(input())
for i in range(num):
    string = input()
    Longeststring(string)
