class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s)<=k:
            return s
        
        while len(s)>k:
            new=""
            for i in range(0,len(s),k):
                temp=s[i:i+k]
                sm=sum(int(ch) for ch in temp)
                new+=str(sm)
            s=new
        
        return s
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # count = 0
        # n = len(s)
        # a= []
        # b= []
        # for i in range(n):
        #     if (s[i:i+k]).split() not in a:
        #         a.append(s[i:i+k].split())
        # m = len(a)
        # for j in range(m):
        #     print(a[j][1])