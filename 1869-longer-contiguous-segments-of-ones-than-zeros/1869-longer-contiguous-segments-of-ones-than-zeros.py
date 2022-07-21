class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s1 = s.split('0')
        s0 = s.split('1')
        r1 = max([len(i) for i in s1])
        r0 = max([len(i) for i in s0])
        return r1>r0
        
        
        
        
        
    
        
        
        
#         count0, count1, a, b  = 0, 0 , [], []
#         n = len(nums)
#         if len(nums) == 1: 
#             if nums[0] == "1":
#                 return True
#             else:
#                 return False
#         for i in range(len(nums)):
#             if nums[i] == '1':
#                 count1 += 1
#                 a.append(count1)
#                 print(a)
#             elif nums[i] == '0':
#                 count0 += 1
#                 b.append(count0)
#                 print(b)
        
#         return max(b)>max(a) 
        