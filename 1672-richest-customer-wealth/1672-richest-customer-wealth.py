class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        b=[]
        for i in range(len(accounts)):
            a = sum(accounts[i])
            b.append(a)
            b.sort()
        return b[-1]
        