class Solution:
    def myAtoi(self, str: str) -> int:
        # Initializing some helper variables/arrays
        INT_MAX = 2**31 - 1
        INT_MIN = (-2)**31
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        specials = ["+", "-"]
        mod = 1

        # Check if string is empty
        if str == "":
            return 0
        
        # 1) Trim leading whitespace
        if str[0] == " ":
            for ch in str:
                if ch == " ":
                    str = str.replace(ch, "", 1)
                else:
                    break
        print(str)
        
        # Check if the resultant string is empty
        if str == "":
            return 0
            
        # 2) Next check that the first character is valid, if not just return 0
        if str[0] not in specials and str[0] not in numbers:
            return 0
        
        # 3) Next pop off the first character
        if str[0] == "-":
            mod = -1
            str = str.replace(str[0], "", 1)
        elif str[0] == "+":
            str = str.replace(str[0], "", 1)
        

        if str == "":
            return 0
        elif str[0] in specials:
            return 0
            

        # 4) Whatever is left is the numerical value we want to convert 
        final_str = ""
        for ch in str:
            if ch in numbers:
                final_str += ch
            else:
                break
        
        if final_str == "":
            return 0
    
        int_str = mod*int(float(final_str))
        print(int_str) 
        if int_str < INT_MIN: 
            return INT_MIN
        elif int_str > INT_MAX:
            return INT_MAX
        else:
            return int_str