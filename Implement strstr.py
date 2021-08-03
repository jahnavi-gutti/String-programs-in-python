#Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s. The function returns and integer denoting the first occurrence of the string x in s (0 based indexing).
str=input()
sub=input()
n=str.find(sub,0,len(str))
if n==-1:
    print("not found")
else:
    print("found")
"""
Output:
geeksfor
fr
not found
"""
