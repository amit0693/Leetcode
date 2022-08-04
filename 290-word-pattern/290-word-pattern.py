class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        x=s.split(' ')
        
        if len(x)!=len(p) : return False
        return len(set(zip(p,x)))==len(set(p))==len(set(x))