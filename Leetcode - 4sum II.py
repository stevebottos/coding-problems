import itertools
import collections

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        
        """
        The idea is to divide and conquer...
        
        After multiple submissions of trying to do this in one single part I've realized that this has to be done in two parts,
        otherwise the time limit is exceeded. The idea is to create a hash map of A and B, then a second hash map of C and D, and use them to determine how 
        many instances of "0 sum" we get
        """
        
        # First get the possible combinations of each element in each list (in two parts) using itertools.product
        combs_AB = itertools.product(A,B)
        combs_CD = itertools.product(C,D)
        
        # Now get the hashes of the sums of the first two lists using collections.Counter (produces a dictionary of schema sum_value : number_of_occurances
        hash_AB_sums = collections.Counter(sum(ab) for ab in combs_AB)
        
        # Since we have the first hash of sums, to keep the second as small as possible we'll only add to this one if - of the sum is in hash_AB_sums
        # ie if the result will be zero
        hash_CD_sums = collections.Counter(sum(cd) for cd in combs_CD if -sum(cd) in hash_AB_sums)

        # This step can be refactored and is completely unnecessary since we're already completely looking through both dictionaries
        # ... Keeping it for clarity
        
        # Now iterate over both dicts and take the product of zero-sum possibilities from each... 
        # ie if there's ONE instance of -1 in one list and THREE instances of one in another, the number of possible zero-sums for that entry is ONE*THREE = THREE
        zero_sum_count = 0
        for i in hash_AB_sums:
            for j in hash_CD_sums:
                if i + j == 0:
                    zero_sum_count += hash_AB_sums[i]*hash_CD_sums[j]

        return zero_sum_count