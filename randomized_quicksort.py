import random


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)


def randomized_quicksort(arr, low, high):
    while low < high:
        pi = randomized_partition(arr, low, high)

        # Same optimization
        if pi - low < high - pi:
            randomized_quicksort(arr, low, pi - 1)
            low = pi + 1
        else:
            randomized_quicksort(arr, pi + 1, high)
            high = pi - 1


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    randomized_quicksort(data, 0, len(data) - 1)
    print("Sorted array:", data)