def stringcheck(string):
    string = list(string)
    l = 0
    r=0

    for i in range(0,len(string)):
        if (string[i] == 'a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i] == 'u'):
            falg =1
        elif not (string[i].isalpha()):
            falg =1
        else:
            if r==0:
                r = i
            else:
                
                string[r],string[i]=string[i],string[r]
                r=0
    return "".join(string)
    
str1 = input()
print(stringcheck(str1))
"""
input:
abc@efg+xyz"
output:
acb@egf+yxza
"""
                
