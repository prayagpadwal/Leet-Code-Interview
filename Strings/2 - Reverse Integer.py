class Solution:
    def reverseString(self, s: List[str]) -> None:

        l = 0 #begining
        r = len(s) - 1 #end

        while l<r: #becasue they should not cross eachother
            s[l], s[r] = s[r], s[l] #interchanging without extra memory
            l += 1 # increment to move forward
            r -= 1 # decrement to move backwar