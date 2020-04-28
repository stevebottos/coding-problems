class Solution:
    
    """
    This one is really easy, the code is self explanatory
    """
    def findLucky(self, arr: List[int]) -> int:

        arr_set = set(arr)
        max_val = -1
        for n in arr_set:
            if n == arr.count(n) and n > max_val:
                max_val = n
                
            
        return max_val