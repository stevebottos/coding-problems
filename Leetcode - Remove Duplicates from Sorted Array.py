class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) != 0:
            max = 1

            # Pointers for the array:
            i = 0
            for j in range(1,len(nums)):
                if nums[i] != nums[j]:
                    i += 1
                    max += 1
                    nums[i] = nums[j]
                    j = i+1
        else:
            max = 0

        return max