num = int(input())
student_record = {}
for i in range(num):
    l = list(map(str,input().split()))
    name,marks = l[0],l[1:]
    marks = map(float,marks)
    student_record[name]=marks
student_name = input()

scorelist = student_record[student_name]
average =0
for i in scorelist:
    average = average+i
result = average/3
print('%.02f'%result)

"""
Input:
 3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

output:
56.00
"""
