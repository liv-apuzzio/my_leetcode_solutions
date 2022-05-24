class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = digits[i] * (10 ** (len(digits) - 1 - i))
        output = list(str(sum(digits) + 1))
        for i in range(len(output)):
            output[i] = int(output[i])
        return(output)