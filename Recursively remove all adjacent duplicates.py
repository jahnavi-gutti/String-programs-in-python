#Given a string s, remove all its adjacent duplicate characters recursively. 
s = input()
s = list(s.rstrip())
n = len(s)
if (n < 2):
	print("")
j = 0
for i in range(n):
	if (s[j] != s[i]):
		j += 1
		s[j] = s[i]
j += 1
s= s[:j]
print(*s, sep = "")
"""		
Output:
jaannuu
janu
"""
