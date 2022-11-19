class Solution(object):
    def myAtoi(self, s):
        upperBound = 2 ** 31
        lowerBound = upperBound * (-1)
        integerCounter = 0
        tenCounter = 1
        idx = 0
        digitStack = []
        length = len(s)
        s = s.strip()
        isNeg = False
        
        if len(s) == 0:
            return 0
        
        if s[0] == '+':
            isNeg = False
            idx = 1
        elif s[0] == '-':
            isNeg = True
            idx = 1
        elif not s[0].isnumeric():
            return 0
        
        if idx >= length or not s[idx].isnumeric():
            return 0
        
        while idx < len(s):
            if s[idx].isnumeric():
                digitStack.append(ord(s[idx]) - 48)
                idx += 1
            else:
                idx = length
                
        while len(digitStack) > 0:
            poppedVal = digitStack[-1]
            digitStack.pop()
            integerCounter += poppedVal * tenCounter
            tenCounter *= 10
            
            
        if isNeg:
            integerCounter *= -1
        
        if integerCounter > upperBound-1:
            return upperBound - 1
        elif integerCounter < lowerBound+1:
            return lowerBound
        else:
            return integerCounter