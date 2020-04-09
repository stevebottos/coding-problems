class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        end = len(nums)-1
        for i in range(0,end):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]