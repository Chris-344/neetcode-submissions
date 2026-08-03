class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i,j in enumerate(arr):
            if i+1<len(arr):
                arr[i]=max(arr[i+1:])
                continue
            arr[i]=-1
        return arr