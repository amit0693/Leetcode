class Solution:
    def heightChecker(self, h: List[int]) -> int:
        h1 = sorted(h)
        print(h, h1)
        count = 0
        for i in range(len(h)):
            if h[i] != h1[i]:
                count += 1
        return count
        
        
#        Use of sorted() instead of h.sort()