class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a = str(num)
        return True if num == 0 else num == int(a[::-1].lstrip('0')[::-1])