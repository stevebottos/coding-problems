class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        string_stack = [s]
        final_stack = []

        while string_stack:
            substr = string_stack.pop()
            
            # A dictionary of dictionaries that will contain keys of characters and then the indexes of groups with those keys
            group_dict = {}
            indices = []
            last_char = None
            for idx, c in enumerate(substr):
                if last_char is None or last_char == c:
                    indices.append(idx)
                else:
                    if not group_dict or last_char not in group_dict:
                        group_dict[last_char] = [indices]
                    else:
                        group_dict[last_char] += [indices]
                    indices = [idx]
                last_char = c
            
            # Handling the last bit
            if not group_dict or last_char not in group_dict:
                group_dict[last_char] = [indices]
            else:
                group_dict[last_char] += [indices]
            
            print(group_dict)
            # Remove the parts that obviously won't work
            reductions = False
            for key in list(group_dict):
                num_chars = 0
                for ilist in group_dict[key]:
                    num_chars += len(ilist)
                if num_chars < k:
                    reductions = True
                    substr = substr.replace(key, "|")
            
            if not reductions:
                final_stack.append(substr)
            else:

                new_strings = substr.split("|")

                for new_string in new_strings:
                    if len(new_string) >= k:
                        string_stack.append(new_string)
            
                        
        max_len = 0
        for f in final_stack:
            if len(f) > max_len:
                max_len = len(f)

        return max_len