class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lMat=0
        rMat=len(matrix)-1
        midM=0

        while lMat <= rMat:
            midM = lMat + (rMat-lMat)//2
 
            if target >= matrix[midM][0] and (target <= matrix[midM][len(matrix[midM])-1]):
                break
            elif target < matrix[midM][0]:
                rMat=midM-1
            else:
                lMat=midM+1

        l=0
        r=len(matrix[midM])-1
        currMatrix=matrix[midM]

        while l <= r:
            mid= l + (r-l)//2
 
            if(currMatrix[mid]==target):
                return True
            elif(currMatrix[mid] < target):
                l=mid+1
            else:
                r=mid-1
        return False