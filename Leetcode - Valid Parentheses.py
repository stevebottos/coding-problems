class Solution:
    def isValid(self, s: str) -> bool:
        
        # Initialize a stack 
        stack = []  # [({

        """
        This variable keeps track of the number of times that we see a "right" expression, ie: ], }, )
        rem should be zero at the end of the program since the right and left brackets should cancel each             other out
        """
        rem = 0
        
        """
        If we see a "left" expression, add it to the stack. 
        If we see a "right" expression, +1 to rem
        If that "right" expression has a matching "left" expression that's valid, -1 to rem and pop
        it from the stack
        If len(stack) = 0 and the value is a "right" bracket, it can't be closed so return false
        """
        for char in s:
            if char in ["[", "(", "{"]:
                stack.append(char)
            elif len(stack) > 0:
                rem += 1
                if char == "]" and stack[-1] == "[":
                    del stack[-1]
                    rem -= 1
                elif char == "}" and stack[-1] == "{":
                    del stack[-1]
                    rem -= 1
                elif char == ")" and stack[-1] == "(":
                    rem -= 1
                    del stack[-1]
            else:
                return False
        
        # check the length of the stack and the value of rem
        if len(stack) == 0 and rem == 0:
            return True
        else:
            return False