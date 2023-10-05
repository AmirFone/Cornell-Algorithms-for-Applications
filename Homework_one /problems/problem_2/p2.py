'''
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
'''
def interval_covering(m,intervals):
    import heapq
    def is_contained(interval, rem_intervals):
        a, b = interval
        for other in rem_intervals:
            if other == interval:
                continue
            start, end = other
            if start <= a and end >= b:
                return True
        return False

    # Sort intervals by end time
    intervals.sort(key=lambda x: (x[1], -x[0]))

    result = []
    while intervals:
        shortest_interval = intervals[0]
        is_redundant = is_contained(shortest_interval, intervals)

        # Remove the interval that has been confirmed as redundant or non-redundant
        intervals.remove(shortest_interval)

        # Only non-redundant intervals are added to the result
        if not is_redundant:
            result.append(shortest_interval)
    result.sort(key=lambda x: (x[1], -x[0]))
    for i in range(1,len(result)-1):
        if result[i-1][1]!=result[i][0]:
            result.pop(i)

    # print(result)
    return result
