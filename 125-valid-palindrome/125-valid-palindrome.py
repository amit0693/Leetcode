class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for i in s:
            if i.isalnum():
                s1+=i.lower()
        
        return s1[::-1] == s1 
        