#Increasing Order Search Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        array = self.inOrder(root)
        if not array:
            return None
        newRoot = TreeNode(array[0])
        curr = newRoot
        for i in range(1, len(array)):
            curr.right =TreeNode(array[i])
            curr = curr.right
        return newRoot

    def inOrder(self, root):
        if not root:
            return []
        array = []
        array.extend(self.inOrder(root.left))
        array.append(root.val)
        array.extend(self.inOrder(root.right))
        return array