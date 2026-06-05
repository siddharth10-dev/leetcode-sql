class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k=k
        self.result=None
        

        def inorder(node):
            if node is None:
                return 

            inorder(node.left)

            self.k = self.k-1
            if self.k == 0:
                self.result=node.val

            inorder(node.right)


        inorder(root)
        return self.result

        