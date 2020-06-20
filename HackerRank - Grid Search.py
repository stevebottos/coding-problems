"""
TODO: The sequence can be repeating in a row, so we need to account for that and search each case in the row to see if it works
Also it fails to account for the case where the check fails on a row but a new start of the sequence is in that row
"""

def gridSearch(G, P):

    p = 0
    target = len(P) - 1 

    for i in range(len(G)):
        row = G[i]
        if p > 0:
            row = row[start_idx:end_idx]
        """
        If the subsequence is found in the row, then search the corresponding indexes
        in the next row to see if it's the next row of the sequence
        """
        if P[p] in row:
            # To get the index if we don't have it already
            if p == 0:
                leading_chars, substr, _ = row.partition(P[p])
                start_idx = len(leading_chars)
                end_idx = start_idx + len(substr)

            if p == target:
                return "YES"
            p += 1

        else:
            p = 0

    return "NO"

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Passes all cases
def gridSearch(G, P):

    
    cols = len(G[0])
    rows = len(G)
    p = 0
    colsP = len(P[0])
    target = len(P)

    
    for c in range(cols-(colsP-1)):
        for r in range(rows):
            if p == target:
                return "YES"

            G_substr = G[r][c:c+colsP]
            P_substr = P[p]
            if G_substr == P_substr:
                print(G_substr, P_substr)
                p += 1
            else:
                p = 0
                P_substr = P[p]
                if G_substr == P_substr:
                    p += 1
        
    # In the event that the sub-array was in the bottom corner of the array:
    if p == target:
        return "YES"
    
    return "NO"
