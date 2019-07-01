#code
def reverse_characters(string):
    # We have convert into list because of the string didn't support
    # assignment symbol.
    string = list(string)
    l = len(string)-1
    r = 0
    while r<l:
        # Didn't disrupt the special characters.
        if not string[r].isalpha():
            r = r+1
        elif not string[l].isalpha():
            l = l-1
        else:
        # swap only the cahracters in the string
            string[r],string[l]=string[l],string[r]
            r=r+1
            l = l-1
            
    return "".join(string)

num = int(input())
for i in range(num):
    s1 = input()
    print(reverse_characters(s1))
    
"""
Input
3
A&B
abc%sld*
dakA&*hA@#N

Output
B&A
dls%cba*
NAhA&*ka@#d
"""
