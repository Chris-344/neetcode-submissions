class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        row=[0] * (amount+1)
        row[-1] = 1
        for n in range(len(coins)-1,-1,-1):
            newRow=[0]*(amount+1)
            newRow[-1] = 1
            for i in range(len(row)-2,-1,-1):
                if i+coins[n]<len(row):
                    newRow[i]=newRow[i+coins[n]]+row[i]
                else:
                    newRow[i]=row[i]
            row=newRow

        return row[0]