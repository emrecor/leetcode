class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s2 = ""
        for c in s:
            if c.isalnum():
                s2+=c
        s1 = s2[::-1]        

        if s2 == s1:
            return True
        return False
        