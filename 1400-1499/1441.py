class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ret = []

        idxT = 0
        idxN = 1
        while idxT < len(target) and idxN <= n:
            ret.append("Push")
            if target[idxT] != idxN:
                ret.append("Pop")
            else:
                idxT += 1

            idxN += 1

        return ret