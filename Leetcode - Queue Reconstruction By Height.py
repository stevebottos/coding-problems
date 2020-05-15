class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if len(people) == 0:
            return []
        
        # The sorting is important
        people = sorted(people)
        
        # Now let's create a hash table that keeps track of how many "greater than" values we have
        hash_table_indices = set([i[0] for i in people])
        ht = {}
        for key in hash_table_indices:
            ht[key] = 0
        del hash_table_indices
        
        # Get the first (smallest) 0-member to start off the stack
        for p in people:
            if p[1] == 0:
                first = p
                people.remove(p)
                break
        
        n = first[0]
        for key in ht:
            if n >= key:
                ht[key] += 1
                    
        # Now we can just treat this as a stack
        stack = [first]
        # Next let's loop through the list that we have an insert when applicable
        while people:
            for el in people:
                if ht[el[0]] >= el[1]:
                    stack.append(el)
                    people.remove(el)
                    n = el[0]
                    break
                    
            for key in ht:
                if n >= key:
                    ht[key] += 1

        return stack
