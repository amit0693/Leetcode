class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        a = []
        an_integer = 1
        strings = [str(integer) for integer in d]
        a_string = "". join(strings)
        an_integer += int(a_string)
        res = list(map(int, str(an_integer)))
        return res