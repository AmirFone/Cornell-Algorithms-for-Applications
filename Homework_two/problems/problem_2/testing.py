import random
import time
import matplotlib.pyplot as plt
from p2_a import closest_pair as closest_a
from p2_b import closest_pair as closest_dp
from p2_c import closest_pair as closest_rand

def generate_random_coordinates_list(size):
    coordinates_list = [(random.uniform(i, i+1), random.uniform(i, i+1)) for i in range(size)]
    return coordinates_list


test_case_n = [10, 50, 100, 250,1000,2000,10000,100000]

runtimes_closest = []
runtimes_closest_dp = []
runtimes_closest_rand = []

for x in test_case_n:
    print("Test Case Size:", x)
    coordinates_list = generate_random_coordinates_list(x)
    
    start_time = time.time()
    closest_a(coordinates_list)
    end_time = time.time()
    runtime_closest = end_time - start_time
    runtimes_closest.append(runtime_closest)

    start_time = time.time()
    closest_dp(coordinates_list)
    end_time = time.time()
    runtime_closest_dp = end_time - start_time
    runtimes_closest_dp.append(runtime_closest_dp)

    start_time = time.time()
    closest_rand(coordinates_list)
    end_time = time.time()
    runtime_closest_rand = end_time - start_time
    runtimes_closest_rand.append(runtime_closest_rand)

    print("Closest Pair:", runtime_closest)
    print("Closest Pair DP:", runtime_closest_dp)
    print("Closest Pair Random:", runtime_closest_rand)
    print("------------------------------------------------------------")

plt.figure(figsize=(10, 6))
plt.plot(test_case_n, runtimes_closest, label='Closest Pair')
plt.plot(test_case_n, runtimes_closest_dp, label='Closest Pair DP')
plt.plot(test_case_n, runtimes_closest_rand, label='Closest Pair Random')

plt.xlabel("Test Case Size")
plt.ylabel("Runtime (seconds)")
plt.legend()
plt.title("Algorithm Runtimes")
plt.grid()
plt.show()
