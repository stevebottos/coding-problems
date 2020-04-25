"""
NOTE THAT THIS IS A WORK IN PROGRESS, IT DOESN'T PASS ALL TEST CASES
... This solution breaks as soon as the seat at 0 or N-1 is removed. The proper solution uses a heap, work through that implementation next.
"""
class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.seats_taken = [0]*N
        

    def seat(self) -> int:
        
        print("- - - - -")
        print(self.seats_taken)
        
        """
        Take care of the obvious cases first:
        1) If the row is empty, sit in the first seat
        2) If the last seat is free, sit there
        
        The next case will compute the max space between two seats
        """
        if self.seats_taken[0] == 0:
            self.seats_taken[0] = 1
            print(0)
            return 0
        elif self.seats_taken[self.N-1] == 0 and sum(self.seats_taken) == 1:
            self.seats_taken[self.N-1] = 1
            print(self.N-1)
            return self.N-1
        else:
            max_dist = 0
            dist = 0
            end_pt = 0
            
            for i in range(self.N):
                # If the seat is empty, the increment the distance by 1 ...
                if self.seats_taken[i] == 0:
                    dist += 1

                # ... Until you reach a non-empty seat ...
                elif self.seats_taken[i] == 1:
                    
                    # ... Then, if there are only two empty seats, then the "true distance" from another person is 1
                    if dist == 2 or dist == 1:
                        true_dist = 1
                    else:
                        true_dist = int(dist-1/2)
                        
                    if true_dist > max_dist:
                        print("ye")
                        end_pt = i-1
                        max_dist = dist
                        
                    print(true_dist, end_pt)
                    dist = 0
                    
            seat_sat_in = end_pt-int(max_dist/2)
            self.seats_taken[seat_sat_in] = 1
            
            print(end_pt, max_dist, seat_sat_in)
            return seat_sat_in

    def leave(self, p: int) -> None:
        self.seats_taken[p] = 0
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
