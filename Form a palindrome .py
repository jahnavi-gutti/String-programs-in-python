"""
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd"""
import sys
def findMinInsertions(str, l, h):
	if (l > h):
		return sys.maxsize
	if (l == h):
		return 0
	if (l == h - 1):
		return 0 if(str[l] == str[h]) else 1

	if(str[l] == str[h]):
		return findMinInsertions(str, l + 1, h - 1)
	else:
		return (min(findMinInsertions(str, l, h - 1),
					findMinInsertions(str, l + 1, h)) + 1)


if __name__ == "__main__":
	
	str = "geeks"
	print(findMinInsertions(str, 0, len(str) - 1))
"""
output:3
"""
