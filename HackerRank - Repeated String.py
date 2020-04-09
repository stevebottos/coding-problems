def repeatedString(s, n):
    
    occurances = 0
    
    # First deal with the whole strings
    multiplier = int(n/len(s))
    num = s.count("a")
    occurances = multiplier*num
    
    # Now the substring
    split = n%len(s)
    s = s[:split]
    num = s.count("a")
    occurances += num
    
    return occurances