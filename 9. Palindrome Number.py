class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>0:
            sayi = str(x)
            sayi1 = sayi[::-1]
            if sayi != sayi1:
                pass
            else:
                return True
        else:
            return False
