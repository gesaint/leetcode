class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # Sort the list
        seqCandies = []
        for item in candies:
            seqCandies.append(item)
        seqCandies.sort(reverse=True)

        # Find the one who just satisfy the greatest number kids
        for idx in range(0, len(seqCandies)):
            if seqCandies[idx] + extraCandies < seqCandies[0]:
                break

        result = []
        if seqCandies[idx] + extraCandies >= seqCandies[0]:
            # All kids with the greatest number of candies
            return [True] * len(candies)
        else:
            for idx2 in range(0, len(candies)):
                if candies[idx2] > seqCandies[idx]:
                    result.append(True)
                else:
                    result.append(False)

        return result

solution = Solution()
#candies = [4,2,1,1,2]
#extraCandies = 1
#candies = [2,3,5,1,3]
#extraCandies = 3
#candies = [2]
#extraCandies = 1
candies = [3, 7]
extraCandies = 5
result = solution.kidsWithCandies(candies, extraCandies)
print(result)