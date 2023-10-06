class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sortedNums = nums.copy()
        sortedNums.sort()
        lIdx = 0
        rIdx = len(sortedNums) - 1

        while (sortedNums[lIdx] + sortedNums[rIdx]) != target:
            if sortedNums[lIdx] + sortedNums[rIdx] > target:
                rIdx -= 1
            elif sortedNums[lIdx] + sortedNums[rIdx] < target:
                lIdx += 1

        ret = []
        for i in range(len(nums)):
            if nums[i] == sortedNums[lIdx]:
                ret.append(i)
            elif nums[i] == sortedNums[rIdx]:
                ret.append(i)

        return ret

solution = Solution()
nums = [2, 7, 11, 15]
target = 17
ret = solution.twoSum(nums, target)
print(ret)