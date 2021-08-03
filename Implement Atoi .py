#Your task  is to implement the function atoi. The function takes a string(str) as argument and converts it to an integer and returns it.

#Note: You are not allowed to use inbuilt function.
string =input()
res = 0
for i in range(len(string)):
	res = res * 10 + (ord(string[i]) - ord('0'))
print(res)"""
Output:
jahnavi
63527657"""
