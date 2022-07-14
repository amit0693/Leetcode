class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        bal = 0
        for i in range(len(s)):
            if s[i] == 'R' :
                bal += 1
            else:
                bal -= 1
                 
            if bal == 0:
                count += 1
        return count
        