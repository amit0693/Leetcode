class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c = set('zxcvbnm')
        z = []
        for i in words:
            f=i.lower()
            if set(f).issubset(b) or set(f).issubset(a) or set(f).issubset(c):
                z.append(i)
        return z