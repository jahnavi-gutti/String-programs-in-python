#Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating another string 'a' by exactly 2 places.
a=input()
b=input()
temp1=" "
temp2=" "

if len(a)<2 or len(b)<2:
    if(a==b):
        print(1)
    else :
        print(0)
temp1=a[2:(len(a))]  +(a[0:2])
temp2=a[(len(a)-2):]+a[0:(len(a)-2)]
if temp1==b or temp2==b:
    print(1)
else:
    print(0)
"""    
Output:
geeksforgeeks
geeksgeeksfor
0
amazon
azonam
1
"""
