class Solution:
    def reverse(self, x: 'int') -> 'int':
        
        # For the case where x is less than zero
        sign = 1
        if x < 0:
            sign = -1
            x = x*(-1)
        
        new = 0
        while x >= 1:
            new += (x%10)
            
            if x >= 10:
                new = new*10
  
            x = int(x/10)
    
        # Checking if it's bigger than the largest int value
        if new > 2147483649:
            new = 0
        return new*sign