class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people)
        max_val = people[-1][0]
        print(max_val)
        
        # Zero members simply need to be sorted based on their first values
        zero_members = [i for i in people if i[1] == 0]
        # Keep this guy sorted too
        leftovers = [i for i in people if i[1] != 0]
        
        
        # Now let's create a hash table that keeps track of how many of each value we have in the current stack
        ht = {}
        for i in range(1,max_val+1):
            ht[i] = 0
        
        for el in zero_members:
            ht[el[0]] += 1
        
        stack = zero_members
        # Next let's loop through the list that we have an insert when applicable
        while leftovers:
            for el in leftovers:
                if ht[el[0]] >= el[1]:
                    print(el)
                    
            break
        
        
        
#         
        
#         # Create a hash table with the count of each thing:
#         ht = {}
        
#         for el in zero_members:
#             key = el[0]
#             if key not in ht:
#                 ht[key] = 1
#             else:
#                 ht[key] += 1
        
#         # Next, insert where applicaple