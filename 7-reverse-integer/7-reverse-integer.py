class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:] 
                temp2 = temp[::-1] 
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)
        # s = str(x)
        # a = ''
        # if s[0] == '-':
        #     a = '-'
        #     s = s.replace('-', '')
        # for i in range(1,len(s)+1):
        #     a += s[-i]
        # return a[1:] if a[0] == '0' else a