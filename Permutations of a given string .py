#Given a string S. The task is to print all permutations of a given strin
from itertools import permutations
s=input()
perm=permutations(s)
for i in perm:
    print("".join(i),end=" ")
"""
Output:
abc
abc acb bac bca cab cba
"""
