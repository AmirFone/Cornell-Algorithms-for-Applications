import time
import random
import matplotlib.pyplot as plt
class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while (i <= self.size):
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while (i >= 1):
            s += self.tree[i]
            i -= i & -i
        return s


def number_of_large_inversions_3a(n, data, delta):
    ordering = data
    count = 0
    for i in range(len(ordering)):
        for j in range(i+1, len(ordering)):
            if ordering[i] > ordering[j] and (j-i) > delta: count += 1
    return count


def number_of_large_inversions_3b(n, data, delta):
    arr = data
    sorted_arr = sorted([(num, i + 1) for i, num in enumerate(arr)], reverse=True)
    fenwick = BIT(n)
    count = 0
    for i, (num, original_idx) in enumerate(sorted_arr):
        # Count of numbers that are greater and positioned more than delta indices before.
        if original_idx - delta - 1 > 0:
            count += fenwick.query(original_idx - delta - 1)
        fenwick.update(original_idx, 1)
    return count

def generate_input(n):
    return [random.randint(1, n) for _ in range(n)]

def timings(function, delta):
    timings = []
    for n in range(0, 1001, 100):  # change the range as needed
        input_data = generate_input(n)
        start = time.time()
        function(n, input_data, delta)
        end = time.time()
        timings.append(end - start)
    return timings

delta = 10
timings_3a = timings(number_of_large_inversions_3a, delta)
timings_3b = timings(number_of_large_inversions_3b, delta)

plt.plot(range(0, 1001, 100), timings_3a, label='number_of_large_inversions_3a')
plt.plot(range(0, 1001, 100), timings_3b, label='number_of_large_inversions_3b')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()
plt.show()
