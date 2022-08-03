class Solution:
    def slowestKey(self, r: List[int], k: str) -> str:
        ans = ""
        mx = prev = 0
        for t, k in zip(r, k):
            mx, ans = max((mx, ans), (t-prev, k))
            prev = t
        return ans