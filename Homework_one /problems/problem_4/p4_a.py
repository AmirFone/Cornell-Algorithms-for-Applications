'''
Problem 4a

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n log n).
'''
def most_frequent_difference_a(values, d_mode) -> int:
    import bisect
    if sum(values)/len(values) == values[0]:
        return len(values)*(len(values)-1)
    values.sort() 
    count = 0
    n = len(values)
  
    for i in range(n):
        j = bisect.bisect_left(values, values[i] + d_mode)
        if j != n and values[j] == values[i] + d_mode:
            count += 1
            
    return count
