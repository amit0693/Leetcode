class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1: return True
        count = 1
        while(count<n):
            count = count * 4
        return count == n