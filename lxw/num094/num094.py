#!/usr/bin/env python3
# coding: utf-8
# FileName: num094.py
# Author: lxw
# Date: 11/5/17 5:00 PM

"""
Num 094: Binary Tree Inorder Traversal
Source: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
# Recursive
class Solution:
    def _in_order_traveral(self, root, result):
        if not root:
            return
        self._in_order_traveral(root.left, result)
        result.append(root.val)        
        self._in_order_traveral(root.right, result)

    def inorderTraversal(self, root):
        """
        Time:  # TODO:
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self._in_order_traveral(root, result)
        return result
'''

# Iterative
# Method 2:
class Solution:
    def inorderTraversal(self, root):
        """
        Time: 52ms. Great.
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []
        while 1:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result


'''
# Method 1:
class Solution:
    def inorderTraversal(self, root):
        """
        Time: 62ms. Tedious and Unreadable.
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        if not root:
            return result
        node = root
        while 1:
            # 1. 循环遍历目标节点target_node的左斜线节点
            while node.left:
                stack.append(node)
                node = node.left

            # 2. node的left为空，node.val入result
            result.append(node.val)

            # 3. 寻找下一个目标节点target_node
            if node.right:
                node = node.right
            else:
                if stack:
                    find = False
                    while stack:
                        node = stack.pop()
                        result.append(node.val)
                        if node.right:
                            node = node.right
                            find = True
                            break
                    if not find:
                        break
                else:
                    break    # The Exit.
        return result
'''


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3
    sol = Solution()
    print(sol.inorderTraversal(node1))

