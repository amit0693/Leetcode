class Solution:
    def secondHighest(self, s: str) -> int:
        a = set()
        for i in s:
            if i.isdigit():
                a.add(int(i))
        a = sorted(a)
        return -1 if len(a) <= 1 else list(a)[-2]
        