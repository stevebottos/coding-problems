class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        # We'll start with initializing a hash table to store the values in terms of their diagonal
        hash_table = {}
        
        # The diagonal which an element belongs to can be obtained as "array_number + index_number"
        # We'll compute the diagonal and just add it to the hash table where it belongs
        for arr_num, arr in enumerate(nums):
            for idx, element in enumerate(arr):
                if arr_num + idx not in hash_table:
                    hash_table[arr_num + idx] = [element]
                else:
                    hash_table[arr_num + idx] = [element] + hash_table[arr_num + idx]
        
        # Finally just run through the hash table and add each key's list to a final list that we will return
        nums_list = []
        for key in hash_table:
            nums_list += hash_table[key]
            
        return nums_list
