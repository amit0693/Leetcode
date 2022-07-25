class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        st = str(num)
        n, count, a  = len(str(num)), 0, []
        for i in range(0, n):
            if len(st[i:k+i]) == k:
                a.append((st[i:k+i]))
        for i in a:
            if int(i) != 0 and num % int(i) == 0 :
                count+=1
        return count