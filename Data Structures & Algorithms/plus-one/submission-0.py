class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        car=1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+car<10:
                digits[i]=digits[i]+car
                car=0
            else:
                digits[i]=(digits[i]+car)%10
                car=1
        if car:
            digits.insert(0,car)
        return digits