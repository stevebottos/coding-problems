class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        str_dict = {}
        slice_start = 0
        
        current_slice = 0
        max_slice = 0
        
        for idx, char in enumerate(s):
            
            current_slice = (idx) - slice_start
            
            if char in str_dict:
                slice_start = max(str_dict[char] + 1, slice_start)
                
            str_dict[char] = idx
            current_slice = (idx+1) - slice_start
            max_slice = max(max_slice, current_slice)

        return max_slice