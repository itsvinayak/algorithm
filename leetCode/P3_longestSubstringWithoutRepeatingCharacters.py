class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] in visited::
                    break
                else:
                    ans = max(ans,j-i+1)
                    visited[s[j]] = True
