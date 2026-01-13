import time

def bubble_sort_descending(arr):
    n = len(arr)

    start_time = time.perf_counter()  # HIGH PRECISION TIMER

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    end_time = time.perf_counter()

    return arr, end_time - start_time


if __name__ == "__main__":

    # LOAD DATASET FIRST (NOT TIMED)
    with open("dataset.txt", "r") as file:
        data = [int(line.strip()) for line in file]

    print("\nSorting in DESCENDING order...\n")

    sorted_data, time_taken = bubble_sort_descending(data.copy())

    print("===== SORTED DATA (DESCENDING) =====")
    for value in sorted_data:
        print(value)

    print(f"\nAlgorithm time taken: {time_taken:.6f} seconds")
