#code
num = int(input())
for i in range(num):
    string = input()
    open_bracket = ['[','{','(']
    close_bracket =[']','}',')']
    l = []
    found =1
    for i in range(0,len(string)):
        if string[i] in open_bracket:
            l.append(string[i])
        elif string[i] in close_bracket:
            pos = close_bracket.index(string[i])
            if len(l)>0 and open_bracket[pos] == l[len(l)-1]:
                l.pop()
            else:
                found=0
                break
    if len(l) ==0 and found==1:
        print('balanced')
    else:
        print('not balanced')
