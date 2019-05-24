#Complete this function
def trappingWater(arr,n):
    #Your code here
    left_max = 0
    left_list =[]
    right_list =[]
    # find the left most height of the building in given list.
    for i in range(0,n):
        left_max = max(arr[i],left_max)
        left_list.append(left_max)
    # find the right most height of the building in given list.
    right_max =0
    for i in range(n-1,-1,-1):
        right_max = max(arr[i],right_max)
        right_list.append(right_max)
    sum1 =0
    # The total trapped water will be summation of the min height of the 
    #left_list and right_list and mius of the current of the height buliding.
    for i in range(0,n):
        sum1 += min(left_list[i],right_list[i]) - arr[i]
    print(sum1)   
