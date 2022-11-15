class Solution:
    def firstUniqChar(self, s: str) -> int:

        dic = {}                # Creating a dictionary

        for i in range(len(s)): # this loop adds all the values and the no. of occurances of that value.
            if s[i] not in dic:         # exxample:
                dic[s[i]] = 1           # a : 2
            else:                       # b : 2
                dic[s[i]] += 1          # c : 1
                                        # d : 1

        for i in range(len(s)): # this loop checks all the values have 1 occurances 
            if dic[s[i]] == 1:  
                return i
        return -1