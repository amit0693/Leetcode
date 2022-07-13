class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0 
        for word in words:
            if all(i in allowed for i in word):
                count +=1
        return count
        
        