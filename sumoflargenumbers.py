#code
# function will be sum of the given large numbers
# number1,number2 are the numbers
def sum_largenumber(number1,number2):
    #before preceding further
    #make sure number2 will large
    if(len(number1)>len(number2)):
        t = number1
        number1 = number2
        number2 = t
    # take empty string
    string =" "
    # length of the given strings
    n1 = len(number1)
    n2 = len(number2)
    # take carry variable
    carry = 0
    number1 = number1[::-1]
    number2 = number2[::-1]
    # chr => will be the changing number to the ascii value
    for i in range(n1):
        sum = ((ord(number1[i])-48) + (ord(number2[i])-48))+carry
        string += chr(sum%10 + 48)
        carry = int(sum/10)
        
    for i in range(n1,n2):
        sum = (ord(number2[i])-48)+carry
        string += chr(sum%10+48)
        carry = int(sum/10)
    if carry:
        string += chr(carry%10+18)
        
    string = string[::-1]
    return string
    
# Take inputs for the user
num = int(input())
for i in range(num):
    string,string1  = map(str,input().split())
    print(sum_largenumber(string,string1))
        
