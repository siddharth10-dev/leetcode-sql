from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        lvl=[]
        q=[root]
        while q !=[] and root is not None:
            for node in q:
                if node.left:
                    lvl.append(node.left)

                if node.right:
                    lvl.append(node.right)
                
            res.append(node.val)
            q=lvl
            lvl=[]

        return res


        