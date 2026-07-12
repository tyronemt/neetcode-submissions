# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = []
        queue.append(root)

        while len(queue) != 0:
            length = len(queue)
            temp = []
            for i in range(length):
                curr = queue.pop(0)
                if curr:
                    temp.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if temp:
                ans.append(temp)
        return ans


