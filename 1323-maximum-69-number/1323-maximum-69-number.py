class Solution:
    def maximum69Number (self, num: int) -> int:
        a = []
        flag= 0
        res = [int(x) for x in str(num)]
        n = len(res)
        for i in range(n):
            a.append(res[i])
            if res[i] == 6 and flag ==0:
                a.pop()
                a.append(9)
                flag = 1
        return int(''.join(str(i) for i in a))
                