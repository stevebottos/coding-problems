class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        
        nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
        total = 0
        subtotal = 0
        ptr = 0
        for i in range(len(s)):
            print(total)
            if s[i] == s[ptr]:
                total += nums[s[i]]
                subtotal += nums[s[i]]
            elif nums[s[i]] > nums[s[ptr]]:
                    subtotal += nums[s[i]]
                    ptr = i
            elif nums[s[i]] < nums[s[ptr]]:
                total += nums[s[i]] - subtotal
                subtotal = 0
                ptr = i
                    
        print('\n')
        return total