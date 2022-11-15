# METHOD 1 -----> : 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): # If the length isnt the same,
            return False     # we return Flase. obviously.

        dic1 = {}            # creating 2 Hashmaps to record
        dic2 = {}            # the number of occurances.

        for i in range(len(s)):
            dic1[s[i]] = 1 + dic1.get(s[i], 0) #using get function 

        for i in range(len(t)):
            dic2[t[i]] = 1 + dic2.get(t[i], 0)

        for c in dic1:
            if dic1[c] != dic2.get(c, 0):
                return False
        return True 

# METHOD 2 -----> :
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)