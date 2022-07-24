class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        a = Counter(r)
        b= Counter(m)
        for i in a:
            
            if b[i] < a[i]:
                return False
        return True