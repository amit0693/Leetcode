import string
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s1 = string.ascii_lowercase
        a =  ""
        
        for i in s:
            a += str(s1.index(i)+1)
        res = [int(x) for x in a]
        x = sum(res)
        if k > 1:
            for i in range(k-1):
                res2 = [int(x) for x in str(x)]
                x = sum(res2)
                
        return x