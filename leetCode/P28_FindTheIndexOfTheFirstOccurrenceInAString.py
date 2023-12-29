class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        c = 0
        for i in range(0, len(haystack)):
            if haystack[i: i+length] == needle :
                return c
            c+=1
        return -1
        
