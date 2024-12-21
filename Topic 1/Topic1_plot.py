import random
import time
import matplotlib.pyplot as plt

def generate_random_intervals(n, max_time=1000):
    intervals = []
    for _ in range(n):
        start = random.randint(0, max_time - 1)
        end = random.randint(start + 1, max_time)  # Ensure end > start
        intervals.append((start, end))
    return intervals

def minimal_announcement_times(intervals):
    intervals.sort(key=lambda x: x[1])
    announcement_times = []
    last_announcement = None
    
    for start, end in intervals:
        if last_announcement is None or last_announcement < start:
            announcement_times.append(end)
            last_announcement = end
    
    return announcement_times

import time

def measure_running_time(input_sizes):
    running_times = []

    for size in input_sizes:
        intervals = generate_random_intervals(size)
        
        # Measure the time to run the algorithm using perf_counter
        start_time = time.perf_counter()
        minimal_announcement_times(intervals)
        end_time = time.perf_counter()
        
        elapsed_time = end_time - start_time
        running_times.append(elapsed_time)
        print(f"Input size: {size}, Running time: {elapsed_time:.6f} seconds")
    
    return running_times


def plot_results(input_sizes, running_times):
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, running_times, marker='o', linestyle='-', color='b')
    plt.title("Running Time vs. Input Size")
    plt.xlabel("Input Size (Number of Intervals)")
    plt.ylabel("Running Time (seconds)")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    input_sizes = [10, 100, 500, 1000, 5000, 10000, 20000]
    
    running_times = measure_running_time(input_sizes)

    plot_results(input_sizes, running_times)
