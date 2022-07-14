import string 
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = string.ascii_lowercase
        for i in s:
            if i not in sentence:
                return False
        return True
        