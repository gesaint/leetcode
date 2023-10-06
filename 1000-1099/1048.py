from typing import List

class Solution:
    # Assume all input is legal and len(subStr) + 1 == len(baseStr)
    def isSubStr(self, subStr, baseStr):
        print("subStr: ")
        print(subStr)
        print("baseStr: ")
        print(baseStr)
        misCnt = 0
        for idx in range(0, len(subStr)):
            if subStr[idx] == baseStr[idx + misCnt]:
                pass
            else:
                misCnt += 1
                if misCnt > 1:
                    print("False")
                    return False
        print("True")
        return True

    def longestStrChain(self, words: List[str]) -> int:
        w_dict = {}

        for word in words:
            if len(word) not in w_dict:
                w_dict[len(word)] = [word]
            else:
                w_dict[len(word)] += [word]

        print(w_dict)

        retList,retCnt = self.getLongestStrChain(w_dict)
        ret = max(retCnt)

        return ret
        
    def getLongestStrChain(self, w_dict):
        lastGroupIdx = list(w_dict.keys())[-1]
        retList = w_dict.pop(lastGroupIdx)
        retCnt = [1] * len(retList)

        if len(w_dict) == 0:
            return retList, retCnt
        
        subList, subCnt = self.getLongestStrChain(w_dict)

        for retIdx in range(0, len(retList)):
            for subIdx in range(0, len(subList)):
                if self.isSubStr(subList[subIdx], retList[retIdx]):
                    subCnt[subIdx] += 1
            
            retCnt[retIdx] = max(subCnt)
        print("retList: ")
        print(retList)
        print("retCnt: ")
        print(retCnt)

        return retList, retCnt


solution = Solution()
words = ['a', 'ab', 'abc', 'cd',"abced", "efg"]
ret = solution.longestStrChain(words)
print(ret)