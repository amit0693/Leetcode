class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a = collections.Counter(arr)
        b = []
        for key, values in a.items():
            if key == values:
                b.append(key)
        return -1 if len(b) == 0 else max(b)
            
    
        