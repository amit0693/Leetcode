class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a = score.copy()
        
        sorted_nums = sorted(score, reverse=True)
        
        for i, item in enumerate(sorted_nums):
            
            if i<=2:
                a[score.index(item)] = ['Gold ', 'Silver ', 'Bronze '][i]+'Medal'
            else:
                a[score.index(item)] = str(i+1)
        return a