class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(product):
            if product < 0:
                return -1
            elif product > 0:
                return 1
            elif product == 0:
                return 0
        count = 1
        for i in nums:
            count *= i
        return signFunc(count)