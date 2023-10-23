class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        lIdx = 0
        ret = 0
        for rIdx in range(1, len(s)):
            for i in range(lIdx, rIdx):
                if s[i] == s[rIdx]:
                    lIdx = i + 1
                    break

            tmp = rIdx - lIdx + 1
            if ret < tmp:
                ret = tmp

        return ret

solution = Solution()
s = "abcabcbb"
ret = solution.lengthOfLongestSubstring(s)
print(ret)