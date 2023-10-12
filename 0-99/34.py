from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        mid = len(nums) // 2
        ret = [-1, -1]
        if nums[mid] < target:
            newNums = nums[mid:]
            ret = self.searchRange(newNums, target)
            if ret[0] != -1:
                ret[0] += mid
                ret[1] += mid
        elif nums[mid] > target:
            newNums = nums[:mid]
            ret = self.searchRange(newNums, target)
        elif nums[mid] == target:
            rNums = nums[mid:]
            rRet = self.searchRange(rNums, target)
            lNums = nums[:mid]
            lRet = self.searchRange(lNums, target)
            if lRet[1] == -1:
                ret[0] = rRet[0] + mid
                ret[1] = rRet[1] + mid
            elif rRet[0] == -1:
                ret[0] = lRet[0]
                ret[1] = lRet[1]
            else:
                ret[0] = lRet[0]
                ret[1] = rRet[1] + mid

        return ret

solution = Solution()
nums = [5,7,7,8,8,10]
target = 8
ret = solution.searchRange(nums, target)
print(ret)