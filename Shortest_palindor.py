def ispalindor(str,st,end):
    # when the st is less than the end directly to the return statement
    while st<end:
        if str[st] != str[end]:
            return False
        st = st+1
        end = end-1
    return True
    
def isfind_no(string,n):
    for i in range(n-1,-1,-1):
        if ispalindor(string,0,i):
            return (n-i-1)
            
num = int(input())
for i in range(num):
    string = input()
    print(isfind_no(string,len(string)))
