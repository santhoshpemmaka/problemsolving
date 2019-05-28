def ispow(num1):
    if num1 ==0:
        return False
    else:
        while num1 != 1:
            if num1 %2 !=0:
                return False
            num1 = num1//2
        return True




num = int(input())
for i in range(num):
    number = int(input())
    result = ispow(number)
    if result == True:
        print("YES")
    else:
        print("NO")
