class Solution:
    def firstUniqChar(self, s: str) -> int:
        for x,y in Counter(s).items():
            if y == 1:
                return s.index(x)
            
        return -1