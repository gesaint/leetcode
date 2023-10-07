from typing import List

class Solution:
    def subIntegerBreak(self, n: int, rlst: List[int]) -> int:
        if n == 1:
            return 1

        ret = 0
        for idx in range(1, n):
            if rlst[n - idx] == 0:
                rlst[n - idx] = self.subIntegerBreak(n - idx, rlst)
            
            tmp = rlst[n - idx] * idx
            if tmp > ret:
                ret = tmp

        if n > ret:
            ret = n
        else:
            rlst[n] = ret

        return ret

    def integerBreak(self, n: int) -> int:
        rlst = [0] * 59

        ret = 0
        for idx in range(1, n):
            if rlst[n - idx] == 0:
                rlst[n - idx] = self.subIntegerBreak(n - idx, rlst)
            
            tmp = rlst[n - idx] * idx
            if tmp > ret:
                ret = tmp

        return ret
            


solution = Solution()
ret = solution.integerBreak(27)
print(ret)