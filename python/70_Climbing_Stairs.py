class Solution:
    def climbStairs(self, n: int) -> int:
        sum1 = 0
        first = 1
        second = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        else:
            for i in range(0, n - 3):
                next1 = first + second
                first = second
                second = next1
                sum1 = first + second
            return sum1