class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_string = ""

        for i in s:
            if i.isalnum(): #this is a DS in py which finds alpha-numeric chars 
                new_string += i.lower() # converting alpha-numeric chars to lower
        return new_string == new_string[::-1] # Reversinging the string
        # Instead of doing (below):
            # if new_string == new_string[::-1]:
            #     return True
            # else:
            #     return False
        # We can just write 'return' and the condition after it
        # if it is true, it will return True 
        # else false 