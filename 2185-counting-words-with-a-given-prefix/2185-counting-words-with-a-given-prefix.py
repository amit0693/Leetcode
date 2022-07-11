class Solution:
    def prefixCount(self, w: List[str], p: str) -> int:
        count = 0
        for i in range(len(w)):
            if w[i][:len(p)] == p:
                count += 1
        return count