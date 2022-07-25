class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True
        count = 1
        while(count<n):
            count = count * 2
        return count == n