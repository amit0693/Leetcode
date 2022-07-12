class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        x=0
        for a in sentences:
            x=max(x,len(a.split()))
        return x
            
        