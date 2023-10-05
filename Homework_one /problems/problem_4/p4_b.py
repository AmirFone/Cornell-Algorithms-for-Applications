'''
Problem 4b

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n).
'''
def most_frequent_difference_b(values, d_mode) -> int:
    freq = {}
    for num in values:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    count = 0
    for num in freq:
        if d_mode == 0:
            count += freq[num] * (freq[num] - 1) 
        else:
            if num - d_mode in freq:
                count += freq[num] * freq[num - d_mode]

    return count