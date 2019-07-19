#code

"""
In clock total will be 360 degree per  60 minutes equals 6 degree per minute,
In clock total will be 360 degree per 12 hours equals 30 degree per minute,
hr_angle = 0.5*(hr*60+min)
min_angle = 6*min
"""
def angle_hour(hr,min1):
    if hr<0 or min1<0 or hr>12 or min1>60:
        return False
        
    if hr == 12:
        hr =0
    if min1 == 60:
        min1=0
        
    hr_angle = 0.5*(hr*60+min1)
    min_angle = min1*6
    angle = abs(hr_angle-min_angle)
    angle = min(360-angle,angle)
    return int(angle)
    
num = int(input())
for i in range(num):
    hr ,min1 = map(int,input().split())
    print(angle_hour(hr,min1))
