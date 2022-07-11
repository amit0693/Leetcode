class Solution:
    def strStr(self, h: str, d: str) -> int: 
        for i in range(len(h)):
            if h[i:i+len(d)] == d:
                return i
        return 0 if d == '' else -1
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # return h.index(d[0]) if d[0] in h and len(h)>len(d) else -1
#         if len(h)>=len(d) and d in h:
#             return h.index(d[0])
#         else:
#             return -1
        