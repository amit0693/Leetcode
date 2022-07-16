class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = len(arr1)
        m = len(arr2)
        a = []
        b=[]
        for i in range(m):
            for j in range(n):
                if arr1[j] == arr2[i]:
                    a.append(arr1[j])
                
        arr1.sort()
        for k in range(n):
            if arr1[k] not in a:
                b.append(arr1[k])
        a.extend(b)
        return a