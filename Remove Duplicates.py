#Given a string without spaces, the task is to remove duplicates from it.

#Note: The original order of characters must be kept the same.
from collections import OrderedDict
str=input()
print ("".join(OrderedDict.fromkeys(str)))
"""
Output:
jannu
janu
"""
