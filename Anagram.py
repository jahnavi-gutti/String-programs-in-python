#Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, “act” and “tac” are an anagram of each other.

a =input()
sa = sorted(a)
a = "".join(sa)
b =input()
sb = sorted(b)
b = "".join(sb)
if a==b:
    print("yes")
else:
    print("no")
"""    
Output:
geeksforg geeks
forgeeksgeeks
yes
"""
