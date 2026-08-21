class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r = 0,len(matrix)-1
        while l<r:
            for i in range(l,r):
                temp=matrix[l][i]
                matrix[l][i]=matrix[r-i+l][l]
                matrix[r-i+l][l]=matrix[r][r-i+l]
                matrix[r][r-i+l]=matrix[i][r]
                matrix[i][r]=temp
            l+=1
            r-=1
