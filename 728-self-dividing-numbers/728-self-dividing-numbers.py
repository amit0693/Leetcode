class Solution:
    def selfDividingNumbers(self, L: int, R: int) -> List[int]:
        A = []
        for x in range(L,R+1):
            str_x = str(x)
            if '0' in str_x:
                continue
            for y in map(int,str_x):
                if x%y:
                    break
            if not x%y:
                A.append(x)
        return A