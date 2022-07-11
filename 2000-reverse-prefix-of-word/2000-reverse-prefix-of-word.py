
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a = word.find(ch)
        b = word[:a+1]
        return b[::-1] + word[a+1:]