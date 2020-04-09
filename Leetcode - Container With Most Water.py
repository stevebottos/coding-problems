class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        
        if len(height) == 2:
            max_fill = min(height)
            
        else:
            # Pointers
            sPtr = 0
            ePtr = len(height)-1

            # Check the ends to ends first
            area = min(height[sPtr], height[ePtr])*(ePtr-sPtr)
            max_fill = area

            while sPtr <= ePtr:
                if height[sPtr] <= height[ePtr] and sPtr < ePtr:
                    sPtr += 1
                    print(sPtr)
                    area = min(height[sPtr], height[ePtr])*(ePtr-sPtr)

                else:
                    ePtr -= 1
                    print(ePtr)
                    area = min(height[sPtr], height[ePtr])*(ePtr-sPtr)

                if area > max_fill:
                    max_fill = area
        print('\n')
        return max_fill
