def find_common_elements(arr1, arr2):
    common_elements = []
    for element in arr1:
        if element in arr2:
            common_elements.append(element)
    return common_elements

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
print(find_common_elements(arr1, arr2))  # Output: [3, 4, 5]
