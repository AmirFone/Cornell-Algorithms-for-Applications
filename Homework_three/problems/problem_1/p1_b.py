# Problem 1b
def bpm(bpGraph, u, matchR, seen):
    for v in range(len(bpGraph[0])):
        # If applicant u is interested in job v and v is not visited 
        if bpGraph[u][v] and seen[v] == False:
            seen[v] = True  # Mark v as visited
            if matchR[v] == -1 or bpm(bpGraph, matchR[v], matchR, seen):
                matchR[v] = u
                return True

    return False

def maximal_bipartite_match(bpGraph):
    matchR = [-1] * len(bpGraph[0])
    result = 0  # Number of jobs assigned to applicants
    for u in range(len(bpGraph)):
        seen = [False] * len(bpGraph[0])
        # If current applicant has not been assigned a job, 
        # then check if a job can be assigned to it or not
        if bpm(bpGraph, u, matchR, seen):
            result += 1
    return result