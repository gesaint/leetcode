# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseSubtree(self, root: Optional[TreeNode], rList: List[int]) -> List[int]:
        retList = [0, 0, 0]
        if root is None:
            return retList

        lList = self.traverseSubtree(root.left, retList)
        rList = self.traverseSubtree(root.right, retList)

        retList[0] = lList[0] + rList[0] + root.val
        retList[1] = lList[1] + rList[1] + 1
        retList[2] = lList[2] + rList[2]
        if retList[0] // retList[1] == root.val:
            retList[2] += 1

        return retList

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        retList = [0, 0, 0]

        retList = self.traverseSubtree(root, retList)

        return retList[2]