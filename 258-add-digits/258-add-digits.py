class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = num % 10 + num // 10
        return num
        
        
        
        
        
        
#         res = [int(x) for x in str(num)]
#         a = len(res)
#         su = []
#         if num ==0: return 0
#         for i in range(a):
#             if len(str(sum(res))) > 1:
#                 res2 = [int(x) for x in str(sum(res))]
#                 su.append(sum(res2))
            
                
#         return su