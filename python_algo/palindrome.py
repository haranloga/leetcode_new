class Solution:
    def isPalindrome(self, x: int) -> bool:         
        if x < 0: 
            return False
        
        if x == 0:
            return True
        

        originalX = x # 121
        numReversed = 0

        while x > 0:
            lastDigit = x % 10 # 1
            numReversed = numReversed * 10 + lastDigit #    121
            x = x // 10 # 12

        return numReversed == originalX

        # 15651





