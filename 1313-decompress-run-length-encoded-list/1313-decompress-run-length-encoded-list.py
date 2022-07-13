class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        b=[]
        for i in range(1,len(nums),2):
            b +=[nums[i]]*nums[i-1]
            
        return b
                
        