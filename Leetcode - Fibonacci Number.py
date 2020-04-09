class Solution:
    def fib(self, N: 'int') -> 'int':
        if N <= 1:
            return N
        else:
            return (Solution.fib(self, N-1) + Solution.fib(self, N-2))