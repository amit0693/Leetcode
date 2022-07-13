class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            if (len(words[i]) == 1):
                return words[i]
            elif(words[i]) == words[i][::-1]:
                return words[i]
            else:
                n = ""
        return n
