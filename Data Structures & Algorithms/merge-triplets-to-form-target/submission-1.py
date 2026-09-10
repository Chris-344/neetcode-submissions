class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        myset=set()
        a,b,c=target

        for i in range(len(triplets)):
            x,y,z=triplets[i]
            if a>=x and b>=y and c>=z:
                myset.add((x,0))
                myset.add((y,1))
                myset.add((z,2))
        return (a,0) in myset and (b,1) in myset and (c,2) in myset