# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Helper function that does literally all the work...
    Dive down the leftmost branch until you either reach the target or the end. If you each the 
    end then backtrack and start exploring the branches from left to right
    """
    def _dfs(node, target):
        
        # If we haven't arrived at a None value, execute the logic below
        if node:
            
            # If this is the target node, return it
            if node.val == target.val:
                return node
            
            """
            If not, continue exploring
            """
            return Solution._dfs(node.left, target) or Solution._dfs(node.right, target)
            
            """
            This doesn't work and I was a fool to think it would... To future me: trace this and understand
            that it provides no way to go back up the tree
            """
            # if node.left:
            #     return Solution.dfs(node.left, target)
            # if node.right:
            #     return Solution.dfs(node.right, target)
            # return None
            
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return Solution._dfs(cloned, target)
    
    
    """
    Note that this can be done in an iterative manner too using stacks as such:
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        stack = [cloned]
        
        while(stack):
            
            cur_node = stack.pop(0)
            
			if cur_node.val == target.val:
                return cur_node
            
			else:
                if cur_node.left != None:
                    stack.append(cur_node.left)
                
                if cur_node.right != None:
                    stack.append(cur_node.right)
                    
    I need practice with recursion though so below is the recursive solution
    """