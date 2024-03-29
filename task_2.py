def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            upper_bound = arr[mid]
            while mid + 1 < len(arr) and arr[mid + 1] == x:
                mid += 1
            return iterations, upper_bound

    return iterations, upper_bound if upper_bound is not None else arr[mid]


def main():
    arr = [1.5, 2.5, 3.7, 5.2, 7.1, 8.9, 10.3]

    def test_binary_search(arr, x):
        print("\nЯ шукаю  значення: ", x)
        iterations, upper_bound = binary_search(arr, x)
        print(f"Кількість ітерацій: {iterations}. Верхня межа: {upper_bound}")

    test_binary_search(arr, 6.2)
    test_binary_search(arr, 5.2)
    test_binary_search(arr, 18.9)
    test_binary_search(arr, -18.9)


if __name__ == "__main__":
    main()
