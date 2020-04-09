class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        nums1.extend(nums2)
        nums = sorted(nums1)
        
        n = len(nums)
        if n%2 == 0:
            idx = int(n/2)-1
            median = (nums[idx] + nums[idx+1])/2   
        else:    
            idx = int(n/2)
            median = nums[idx]
 
        return median
                