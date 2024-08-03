def binary_search_signal(signal, target):
    """
    Searches for a target value in a sorted signal using the binary search algorithm.

    Parameters:
    signal (list): The sorted signal to be searched.
    target (int): The target value to search for.

    Returns:
    int: The index of the target value in the signal, or -1 if not found.
    """
    left, right = 0, len(signal) - 1
    while left <= right:
        mid = (left + right) // 2
        if signal[mid] == target:
            return mid
        elif signal[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
signal = [11, 12, 22, 25, 34, 64, 90]
index = binary_search_signal(signal, 25)
print("Index of 25 in signal using Binary Search:", index)
