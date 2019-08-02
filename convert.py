"""
These three words will be read one at a time, in three separate line
The first word should be changed like all vowels should be replaced by %
The second word should be changed like all consonants should be replaced by #
The third word should be changed like all char should be converted to upper case
Then concatenate the three words and print them
 h%wa#eYOU.
"""
str1 = input()
str2 = input()
str3 = input()
str1 = list(str1) 
str2 = list(str2)
str3 = list(str3)
for x in range(len(str1)):
    if str1[x] == 'a' or str1[x] == 'A' or str1[x] == 'e' or str1[x]=='E' or str1[x]=='O' or str1[x] == "o" or str1[x]=='i' or str1[x] == "I" or str1[x] == 'U' or str1[x]=="u":
        str1[x] = "%"
for x in range(len(str2)):
    if not (str2[x] == 'a' or str2[x] == 'A' or str2[x] == 'e' or str2[x]=='E' or str2[x]=='O' or str2[x] == "o" or str2[x]=='i' or str2[x] == "I" or str2[x] == 'U' or str2[x]=="u"):
        str2[x] = "#"
for x in range(len(str3)):
    if str3[x].islower():
        str3[x] = str3[x].upper()
result = ""
str1 = "".join(str1)
str2 = "".join(str2)
str3 = "".join(str3)
print(str1+str2+str3)
