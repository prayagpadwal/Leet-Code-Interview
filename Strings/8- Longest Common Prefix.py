class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chars = zip(*strs)
        res = ""

        for c in chars:
            if len(set(c)) == 1:
                res += c[0]
            else:
                break
        return res