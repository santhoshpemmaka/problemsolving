"""
     #
    # #
   #   #
  #     #
 #       #
#         #
###########  
"""
def pattern(num):
    for i in range(num):
        str1 = []
        for j in range(num*2-1):
            if j == ((num*2-1)//2)-i:
                str1.append("#")
            elif j==((num*2-1)//2)+i:
                str1.append("#")
            else:
                str1.append(" ")
        print("".join(str1))
    for i in range(num*2-1):
        print("#",end="")
    
pattern(6)
        
