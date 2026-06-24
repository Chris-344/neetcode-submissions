class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c=0
        d,u=0,len(matrix)-1
        while u >= d:
            c = d + (u - d) // 2
            if target >= matrix[c][0] and target <= matrix[c][-1]:
                break
            elif target > matrix[c][-1]:
                d=c+1
            elif target < matrix[c][0]:
                u=c-1

        if not(d <= u):
            return False

        arr=matrix[c]
        l,r=0,len(arr)-1
        
        while l <= r:
            m = l + (r-l)//2
            if arr[m] < target:
                l=m+1
            elif arr[m] > target:
                r=m-1
            else:
                return True
        return False