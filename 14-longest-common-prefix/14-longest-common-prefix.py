class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        same=''
        l = [len(st) for st in strs] 
        if len(strs)>=2:
            for i in range(min(l)): 
                tmp = [s[i] for s in strs] 
                if min(tmp)==max(tmp):
                    same += tmp[0]
                else:
                    return same
            return same
        else:
            return strs[0]
        
                
                
                                  