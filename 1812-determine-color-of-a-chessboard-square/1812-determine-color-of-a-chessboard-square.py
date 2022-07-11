class Solution:
    def squareIsWhite(self, c: str) -> bool:
        a = "aceg"
        b = "bdfh"
        if c[0] in a and int(c[1])%2!=0:
            return False
        elif c[0] in b and int(c[1])%2==0:
            return False
        else:
            return True
            