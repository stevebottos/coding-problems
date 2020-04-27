class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        hash_table = {}
        
        for arr_num, arr in enumerate(nums):
            for idx, element in enumerate(arr):
                if arr_num + idx not in hash_table:
                    hash_table[arr_num + idx] = [element]
                else:
                    hash_table[arr_num + idx] = [element] + hash_table[arr_num + idx]
        
        nums_list = []
        for key in hash_table:
            nums_list += hash_table[key]
            
        return nums_list