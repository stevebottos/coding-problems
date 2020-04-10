class Solution:
    
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        # Right away let's handle this case (single element):
        if len(grid[0]) == 1 and len(grid) == 1:
            return True
        
        # There are 12 possible moves - two for each street depending on where you enter
        # Dictionary stores in format (streetcode_input-direction : input-direction, (transform-index-0, transform-index_1),  output-direction)
        move_dict = {"1_right" : ("right", (0,1), "right"),
                     "1_left" : ("left", (0,-1), "left"),
                     "2_up" : ("up", (-1,0), "up"),
                     "2_down" : ("down", (1,0), "down"),
                     "3_right" : ("right", (1,0), "down"),
                     "3_up" : ("up", (0,-1), "left"),
                     "4_up" : ("up", (0,1), "right"),
                     "4_left" : ("left", (1,0), "down"),
                     "5_right" : ("right", (-1,0), "up"),
                     "5_down" : ("down", (0,-1), "left"),
                     "6_down" : ("down", (0,1), "right"),
                     "6_left" : ("left", (-1,0), "up")
                    }
        
        # Handle initial cases since these don't have an input direction
        possible_directions = []
        if grid[0][0] == 1:
            possible_directions = ["right"]
        elif grid[0][0] == 2:
            possible_directions = ["down"]
        elif grid[0][0] == 3:
            possible_directions = ["right"]
        elif grid[0][0] == 4:
            possible_directions = ["up", "left"]
        elif grid[0][0] == 5:
            return False
        elif grid[0][0] == 6:
            possible_directions = ["down"]
        
        cols = len(grid[0])
        rows = len(grid)
        n_moves = (rows*cols) 
        path_valid = False
        
        for d in possible_directions:
            target_destination_on_path = False
            path_traversable = True
            direction = d
            pos = [0,0]
            mod = (0,0)
            for i in range(n_moves):
                if (pos[0] >= rows) or (pos[1] >= cols):
                    break
                street_type = grid[pos[0]][pos[1]]
                state_key = str(street_type) + "_" + direction
                if state_key in move_dict:
                    mod = move_dict[state_key][1]
                    pos[0] += mod[0]
                    pos[1] += mod[1]
                    direction = move_dict[state_key][2]
                    
                    if pos[0] == rows-1 and pos[1] == cols-1:
                        target_destination_on_path = True
                else:
                    path_traversable = False
                    break

            if target_destination_on_path and path_traversable:
                return True
        
        return target_destination_on_path and path_traversable