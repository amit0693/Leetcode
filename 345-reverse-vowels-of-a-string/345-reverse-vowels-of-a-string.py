class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
        
        
        
        
        
        
#         a = 'AEIOUaeiou'
#         b = []
#         c = list(s)
#         for i in s:
#             if i in a:
#                 b.append(i)
#         b.reverse()
#         print(c, b)
#         for i in range(len(c)):
#             if c[i] in a:
#                 for j in range(len(b)-1):
#                     c[i] = b[j]
#                     b.pop(j)
#         return c
                    
        
        
#         b = []
#         c = list(s)
#         for i in s:
#             if i in a:
#                 b.append(i)
#         b.reverse()
#         print(b)
#         for i in range(len(c)):
#             print(c[i] in b)
                