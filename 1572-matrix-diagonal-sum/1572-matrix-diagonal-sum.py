class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count=0
        n = len(mat)
        for i in range(n):
            count +=mat[i][i]+mat[i][n-i-1]
        print(count)
        if(n%2==0):
            return count;
        else:
            return count-mat[n//2][n//2];