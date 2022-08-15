class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s = (title.lower()).split()
        for i in range(len(s)):
            if len(s[i])>2:
                s[i]=(s[i][0]).upper()+s[i][1:]
        return ' '.join(s)