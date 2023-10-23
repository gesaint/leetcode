class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False

        bn = bin(n)[2:]
        
        # 1 00 00
        if len(bn) % 2 == 0:
            return False 
        
        bn = bn[1:]

        sum = 0
        for i in range(len(bn)):
            sum += int(bn[i])

        if sum == 0:
            return True

        return False


solution = Solution()
#n = 16
#n = 17
n = 64
ret = solution.isPowerOfFour(n)
print(ret)