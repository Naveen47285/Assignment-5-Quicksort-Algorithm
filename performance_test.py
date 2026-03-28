import time
import random
import matplotlib.pyplot as plt
from quicksort import quicksort
from randomized_quicksort import randomized_quicksort


def generate_data(size, case_type):
    if case_type == "random":
        return [random.randint(0, 10000) for _ in range(size)]
    elif case_type == "sorted":
        return list(range(size))
    elif case_type == "reverse":
        return list(range(size, 0, -1))


def measure_time(sort_func, data):
    start = time.time()
    sort_func(data, 0, len(data) - 1)
    return time.time() - start


sizes = [1000, 2000, 5000]
cases = ["random", "sorted", "reverse"]

results = {}

for case in cases:
    results[case] = {"deterministic": [], "randomized": []}

    print(f"\nCase: {case}")
    for size in sizes:
        data1 = generate_data(size, case)
        data2 = data1.copy()

        # Deterministic
        t1 = measure_time(quicksort, data1)

        # Randomized
        t2 = measure_time(randomized_quicksort, data2)

        results[case]["deterministic"].append(t1)
        results[case]["randomized"].append(t2)

        print(f"Size {size}: Deterministic={t1:.5f}, Randomized={t2:.5f}")


# 📊 Plot results
for case in cases:
    plt.figure()
    plt.plot(sizes, results[case]["deterministic"], label="Deterministic")
    plt.plot(sizes, results[case]["randomized"], label="Randomized")

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Performance Comparison ({case} data)")
    plt.legend()
    plt.grid()

    plt.savefig(f"{case}_performance.png")

plt.show()