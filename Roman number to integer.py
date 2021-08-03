#Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
"""
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
"""
def romanToInt(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i = 0
    num = 0
    while i < len(s):
        if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
        else:
            num+=roman[s[i]]
            i+=1
    return num
print(romanToInt("III"))
print(romanToInt("XLIX"))
"""
Output:
3
49
"""
