# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        rootref = root
        if not root:
            return None
        #if root
        
        def recursion(node,key):
            if not node:
                return node
            
            if node.val < key: 
                node.right = recursion(node.right,key)
            elif node.val > key:
                node.left = recursion(node.left,key)
            else:
                if not node.right and not node.left:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:

                    cur = node.right
                    while cur.left:
                        cur = cur.left
                    node.val = cur.val
                    node.right = recursion(node.right,cur.val)
            return node
        
        return recursion(root,key)
        
        