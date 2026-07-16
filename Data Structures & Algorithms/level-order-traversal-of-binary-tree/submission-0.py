# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs 
        res = []
        q = [root]
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                cur = q.pop(0)
                if not cur:
                    continue
                level.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            if level:
                res.append(level)
        return res
            
            