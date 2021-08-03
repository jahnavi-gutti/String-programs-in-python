#Given a string S, find length of the longest substring with all distinct characters

class Solution:
   def solve(self, s):
      from collections import Counter
      start = 0
      c = Counter()
      ans = 0
      for end in range(len(s)):
         c[s[end]] += 1
         while len(c) > 2:
            c[s[start]] -= 1
            if not c[s[start]]:
               del c[s[start]]
            start += 1
         ans = max(ans, end - start + 1)
      return ans
ob = Solution()
s = "xyzzy"
print(ob.solve(s))"""
Output:
4""
