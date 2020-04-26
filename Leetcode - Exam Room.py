class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.seats_taken = []
        

    def seat(self) -> int:
        
        # If there's nobody currently seated, sit in the first seat
        if len(self.seats_taken) == 0:
            sit_at = 0
        # If only the first seat is taken, 
        elif len(self.seats_taken) == 1 and self.seats_taken[0] == 0:
            sit_at = self.N-1
        else:
            max_dist = -1
            sit_at = 0
            
            if 0 not in self.seats_taken:
                dist = self.seats_taken[0]
                if dist > max_dist:
                    sit_at = 0
                    max_dist = dist
                    
            for i in range(len(self.seats_taken) - 1):
                    pair = (self.seats_taken[i], self.seats_taken[i+1])
                    dist = (pair[1] - pair[0]) // 2
                    if dist > max_dist:
                        sit_at = pair[0] + dist
                        max_dist = dist
                        
            if self.N-1 not in self.seats_taken:
                dist = self.N-1 - self.seats_taken[-1]
                if dist > max_dist:
                    sit_at = self.N-1
                    max_dist = dist
        
        bisect.insort(self.seats_taken, sit_at)
        return sit_at
                
                

    def leave(self, p: int) -> None:
        self.seats_taken.remove(p)
