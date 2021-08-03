#Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index).

s=input().strip()
n=len(s)
l=[]
for i in range(len(s)):
    if s[0:n-i]==s[n-i-1::-1]:
        #print(s[0:n-i])
        l.append(s[0:n-i])
          
    if s[n-i:]==s[:n-i-1:-1] and s[n-i:]!="":
        #print(s[n-i:])
        l.append(s[n-i:])
print(l)
print(max(l))
"""
Output:	
aabaa
['aabaa', 'a', 'aa', 'aa', 'a']
aabaa
"""

