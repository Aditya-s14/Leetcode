class Solution:
    def isPalindrome(self, x: int) -> bool:
        copy  = x
        res=0
        if x<0:
            return False
        while x!=0:
            rem = x%10
            x//=10
            res=(res*10)+rem
        if res==copy:
            return True
        else:
            return False

        
        