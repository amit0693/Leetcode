class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count=0
        for i in range(len(operations)):
            if "++" in operations[i]:
                count +=1
            else:
                count -=1
        return count
            