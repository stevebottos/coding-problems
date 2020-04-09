class Solution:
    def missingNumber(self, nums: 'List[int]') -> 'int':    
        # Create a sorted version of A
        B = sorted(nums)

        # Initialize an array to hold the positive values of B only. If there are none, C will remain empty
        C = []
        for i in range(len(B)):
            if B[i] >= 0:
                min = B[i]
                C = B[i:len(B)]
                break

        # If C is empty then the array has no positive values and the max will be 1
        n = len(C)

        # Cases where there are no positive values or the starting value of the list is greater than 0
        if n == 0 or min > 0:
            min = 0
        else:
            for k in range(n):
                if min == C[k]:
                    min = C[k] + 1

        return min