class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        ret = 0

        for j in range(len(nums)):
            for i in range(j):
                if nums[i] == nums[j]:
                    ret += 1

        return ret



nums = [1, 2, 3, 1, 1, 3]
solution = Solution()
ret = solution.numIdenticalPairs(nums)
print(ret)
