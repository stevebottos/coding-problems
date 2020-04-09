class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return [nums]
        
        n = len(nums)
        perm = []
        
        for i in range(n):
            obj_at_i = nums[i]
            other_elements_in_list = nums[:i] + nums[i+1:]
            
            for partial_permutation in Solution.permute(self, other_elements_in_list):
                perm.append([obj_at_i] + partial_permutation)
                
        return perm
