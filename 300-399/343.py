class Solution:
    def subIntegerBreak(self, n: int) -> int:
        if n <= 1:
            return n

        ret = 0
        for i in range(1, n):
            tmp = self.subIntegerBreak(n - i) * i
            if tmp > ret:
                ret = tmp

        if ret < n:
            return n

        return ret

    def integerBreak(self, n: int) -> int:
        ret = 0
        for i in range(1, n):
            tmp = self.subIntegerBreak(n - i) * i
            if tmp > ret:
                ret = tmp

        return ret
    
solution = Solution()
ret = solution.integerBreak(27)
print(ret)