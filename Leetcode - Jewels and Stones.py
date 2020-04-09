class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        
        count = 0
        for i in range(len(J)):
            if J[i] in S:
                for k in range(len(S)):
                    if S[k] == J[i]:
                        count += 1
                        
        return count