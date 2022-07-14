class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict = Counter(s)
        a = list ( dict.values())
        for i in range(len(a)-1):
            if a[i] != a[i+1]:
                return False
        return True