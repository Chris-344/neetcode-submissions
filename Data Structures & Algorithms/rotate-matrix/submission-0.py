class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l=0
        r=len(matrix)-1
        
        while l<r:
            for i in range(l,r):
                temp=matrix[l][i]
                matrix[l][i]=matrix[l+r-i][l]
                matrix[l+r-i][l]=matrix[r][l+r-i]
                matrix[r][l+r-i]=matrix[i][r]
                matrix[i][r]=temp
            l+=1
            r-=1