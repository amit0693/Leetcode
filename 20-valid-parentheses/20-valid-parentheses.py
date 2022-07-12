class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "]" : "[", "}" : "{"}
        q = deque()
        
        for ch in s:
            if ch in d.keys() and q:
                if d[ch] == q.pop():
                    pass
                else:
                    return False
            else: 
                q.append(ch)
        
        if not q:
            return True
            