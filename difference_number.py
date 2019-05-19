#code
# python3 find the difference between the two given large numbers

def substractor(str1,str2):
    
    n1 = len(str1)
    n2 = len(str2)
    if n1 < n2:
        return True
    elif n1 > n2:
        return False
    for i in range(n1):
        if str1[i]<str2[i]:
            return True
        else:
            return False

# function of the difference numbers

def difference_numbers(string,string1):
    
    if (substractor(string,string1)):
        t = string
        string = string1
        string1 = t
        
    # length of the strings
    n = len(string)
    n1 = len(string1)
    
    string = string[::-1]
    string1 = string1[::-1]
    
    carry = 0
    result = ""
    
    for i in range(n2):
        sub = (ord(string[i])-48) - (ord(string1[i])-48) - carry
        
        # if sub is the less than "0" added to the 10 and carry 1
        # carry will be 0
        
        if sub <0:
            sub += 10
            carry =1
        else:
            carry = 0
        
        result += str(sub)
        
    for i in range(n2,n1):
        sub = (ord(string[i])-48) - carry
        
        if sub < 0:
            sub += 10
            carry =1
        else:
            carry = 0
        
        result += str(sub)
        
    result = result[::-1]
    
    return result
    
num = int(input())
for i in range(0,num):
    number,number1 = map(str,input().split())
    print(difference_numbers(number,number1))
    

    
