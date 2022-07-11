class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        i = j = 0
        result = ""
        while i < len(w1) and j < len(w2):
           result += w1[i] + w2[j]
           i+=1
           j+=1
        while i < len(w1):
           result += w1[i]
           i += 1
        while j < len(w2):
           result += w2[j]
           j += 1
        return result