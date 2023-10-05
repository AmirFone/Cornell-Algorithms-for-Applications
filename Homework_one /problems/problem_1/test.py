import time
import random
import matplotlib.pyplot as plt
from p1_b import stable_matching_1b
from p1_c import stable_matching_1c
import statistics
import tempfile

sizes = [25, 50, 100, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2500, 3000,4000,10000]


problem_1b_times = []
problem_1c_times = []

for n in sizes:
    doctor_preferences = []
    hospital_preferences = []
    for i in range(n):
        pref = list(range(0, n))
        random.shuffle(pref)
        doctor_preferences.append(pref)
        random.shuffle(pref)
        hospital_preferences.append(pref)
    temp = tempfile.NamedTemporaryFile()

    with open(temp.name, "w") as f:
        line = f"{n}\n"
        f.write(line)
        for pref in doctor_preferences:
            line = " ".join(map(str, pref)) + "\n"
            f.write(line)
        for pref in hospital_preferences:
            line = " ".join(map(str, pref)) + "\n"
            f.write(line)

    test_times = []
    print("1b for n = {}".format(n))
    for _ in range(1):
        start_time = time.time()
        stable_matching_1b(temp.name)
        end_time = time.time()
        test_times.append(end_time - start_time)
    problem_1b_times.append(statistics.median(test_times))

    test_times = []
    print("1c for n = {}".format(n))
    for _ in range(1):
        start_time = time.time()
        stable_matching_1c(temp.name)
        end_time = time.time()
        test_times.append(end_time - start_time)
    problem_1c_times.append(statistics.median(test_times))

plt.figure(figsize=(10, 8)) 

plt.plot(sizes, problem_1c_times, marker='x', label='Gale-Shapley', color='green')
plt.plot(sizes, problem_1b_times, marker='o', label='1b', color='blue')

plt.xlabel('Input Size N')
plt.ylabel('Time (seconds)')
plt.title('Gale-Shapley vs B1')
plt.legend()

plt.grid(True, which="both", ls="--", c='0.50')

plt.savefig('gale_shapley_vs_man_oriented.png', dpi=350)
plt.show()