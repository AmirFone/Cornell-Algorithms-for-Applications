import time
import random
import matplotlib.pyplot as plt
# from homework.hw0.code.problems.problems_1.p1_advanced import linear_search, binary_search
from p1_advanced import linear_search, binary_search

sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000]
# generate random lists of different sizes to test
random_lists = [[random.randint(0, 1_000_000) for i in range(size)] for size in sizes]

linear_times = []
binary_times = []

for random_list in random_lists:
    # need to sort the list for binary search
    sorted_random_list = sorted(random_list)

    # Time linear search
    start = time.time()
    linear_search(sorted_random_list, sorted_random_list[random.randint(0, len(sorted_random_list) - 1)])
    end = time.time()
    linear_times.append(end - start)

    # Time binary search
    start = time.time()
    binary_search(sorted_random_list, sorted_random_list[random.randint(0, len(sorted_random_list) - 1)])
    end = time.time()
    binary_times.append(end - start)

# Plotting
plt.plot(sizes, linear_times, label="Linear Search")
plt.plot(sizes, binary_times, label="Binary Search")
plt.xlabel("List Size")
plt.ylabel("Time (s)")
plt.title("Linear vs Binary Search")
plt.legend()
plt.show()