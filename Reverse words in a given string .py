#Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

str_arr = input().split(".")
print(".".join(str_arr[::-1]))
"""
Output:
i.l.o.v.e.m.e
e.m.e.v.o.l.i
"""
