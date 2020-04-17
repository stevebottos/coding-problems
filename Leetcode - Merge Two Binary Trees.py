# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        # Tree 1 will be the one that we update
        stack = []
        
        # The cases where there isn't another tree:
        if not t1:
            return t2
        
        if not t2:
            return t1
        
        """
        The meat of the program. Just yesterday I did a problem involving a dfs so I won't use recursion             here.
        Instead, I'll work through the implementation that utilizes stacks.
        
        The stack will either contain a node pair or a single node. t1 will be the tree that we modify in             place and return at the end. You really only have to worry about the folowing scenarios:
        
        1) If t1 and t2 overlap, modify t1 in place as t1.val += t2.val
        2) If there is no node for t1 but there is for t2, "remove" that node from t2 and put it onto t1
        with all of its connections etc
        
        ... If there is a node for t1 but not for t2 we don't have to care, since t1 is the tree we're returning
        """
        
        stack = [[t1, t2]]
        while stack:

            pair = stack.pop()
            if pair[0] and pair[1]:
                pair[0].val += pair[1].val
                
                if pair[0].left and pair[1].left:
                    stack.append([pair[0].left, pair[1].left])
                elif pair[1].left and not pair[0].left:
                    pair[0].left = pair[1].left
                    stack.append([pair[0].left, None])
                    
                if pair[0].right and pair[1].right:
                    stack.append([pair[0].right, pair[1].right])
                elif pair[1].right and not pair[0].right:
                    pair[0].right = pair[1].right
                    stack.append([pair[0].right, None])
            
        return t1