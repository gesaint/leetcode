class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ls = list(s)
        idx1 = 0
        for i in range(len(ls)):
            if ls[i] == '#':
                if idx1 > 0:
                    idx1 -= 1
            else:
                ls[idx1] = ls[i]
                idx1 += 1

        lt = list(t)
        idx2 = 0
        for i in range(len(lt)):
            if t[i] == '#':
                if idx2 > 0:
                    idx2 -= 1
            else:
                lt[idx2] = lt[i]
                idx2 += 1

        if idx1 == 0 and idx2 == 0:
            return True

        print(ls[:idx1])
        print(lt[:idx2])
        if ls[:idx1] == lt[:idx2]:
            return True

        return False


solution = Solution()
s = "ab#c"
t = "ad#c"
#s = "a#c"
#t = "b"
ret = solution.backspaceCompare(s, t)
print(ret)