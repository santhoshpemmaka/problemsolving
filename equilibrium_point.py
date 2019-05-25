#code
def Equilibrium_point(arr):
    # return the index of the array asssume starting 1
    if len(arr)==1:
        return 1
    else:
        
        left_sum,right_sum=0,0
    
        length = len(arr)
        # Sum of the array starting for the index 1 to len(arr)
        for i in range(1,length):
            right_sum += arr[i]
        
        
        i,j = 0,1
        while j<length:
        #  Decerase form right_sum by the j postion
            right_sum -= arr[j]
        # Adding by the left_sum by the  i postion
            left_sum += arr[i]
        
        # compare left_sum equal to the right_sum return index i+2
            if left_sum == right_sum:
                return i+2
            
            i+=1
            j+=1
        return -1
    
# main program of the problem
num = int(input())
for i in range(0,num):
    number = int(input())
    array = list(map(int,input().split()))
    print(Equilibrium_point(array))

