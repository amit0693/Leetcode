class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for l in s:
            if l not in t:
                return False
            i = t.find(l)
            t = t[i+1:]
        return True