class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0 

        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: 1 + len(needle)] == needle:
                return i
        if(haystack.length() < needle.length() ):
            return -1
        return -1