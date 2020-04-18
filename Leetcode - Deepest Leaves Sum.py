# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    """
    As it turns out this is actually a pretty solid solution - faster than 92% and less memory than 100%.
    
    The idea is really simple to conceptualize - just store each layer of the tree in a dictionary,
    where the entry at dict[n] are the nodes of the tree at that level. We can do this with a while loop.
    If there are no nodes at any position at a certain level in the tree, that spot will be filled with a 
    None value.
    
    We know we've reached the end of the tree if we encounter a level with all None values,
    ie dict[N] = [None, ... , None]. In this case just move to dict[n-1] and take the sum of all of the
    non-none values at that level and that's the answer.
    """
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth_dict = {}
        depth_dict[0] = []
        if root.left:
            depth_dict[0].append(root.left)
        if root.right:
            depth_dict[0].append(root.right)

        n = 1
        tree_remaining = True
        while tree_remaining:
            tree_remaining = False
            depth_dict[n] = []
            for i in depth_dict[n-1]:
                if i:
                    tree_remaining = True
                    depth_dict[n].extend([i.left, i.right])
            
            if tree_remaining == False:
                # Remove the empty list entry
                del depth_dict[n]
                n -= 1
                # Remove the all-None entry:
                del depth_dict[n]
                n -= 1
            else:
                n += 1
            
        total_bottom = 0
        for node in depth_dict[n]:
            if node:
                total_bottom += node.val
                
        return total_bottom