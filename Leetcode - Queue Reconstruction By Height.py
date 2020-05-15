# Test case failed on: [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # The sorting is important
        people = sorted(people)
        
        # Some additional starting values 
        zero_members = [i for i in people if i[1] == 0]
        leftovers = [i for i in people if i[1] != 0]
        hash_table_indices = set([i[0] for i in people])
        
        # Now let's create a hash table that keeps track of how many "greater than" values we have
        ht = {}
        for key in hash_table_indices:
            ht[key] = 0
    
        del hash_table_indices
    
        # Now let's start with the zero members since they're simply inserted into the table in order
        for el in zero_members:
            n = el[0]
            print(n)
            for key in ht:
                if n >= key:
                    ht[key] += 1
                
        
        # Now we can just treat this as a stack
        stack = zero_members
        # Next let's loop through the list that we have an insert when applicable
        while leftovers:
            for el in leftovers:
                if ht[el[0]] >= el[1]:
                    stack.append(el)
                    leftovers.remove(el)
                    n = el[0]
                    break
                    
            for key in ht:
                if n >= key:
                    ht[key] += 1
            
        
        return stack
