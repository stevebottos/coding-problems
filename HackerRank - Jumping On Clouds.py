def jumpingOnClouds(c):
    # First check the length. Since the game is always able to be completed then if len is 2 return 1
    if len(c) == 2:
        return 1

    jumps = 0
    ptr = 0
    end_of_clouds = False
    while end_of_clouds == False:
        if ptr < (len(c)-2) and c[ptr+2] == 0:
            jumps += 1
            ptr += 2
        elif ptr < (len(c)-1) and c[ptr+1] == 0:
            jumps += 1
            ptr += 1
        else:
            end_of_clouds = True
        print(ptr, jumps)
            
    return jumps