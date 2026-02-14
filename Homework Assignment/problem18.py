def commonElements(arr1, arr2, arr3):
    i = j = k = 0
    n1, n2, n3 = len(arr1), len(arr2), len(arr3)
    result = []

    while i < n1 and j < n2 and k < n3:

        # Skip duplicates in arr1
        if i > 0 and arr1[i] == arr1[i - 1]:
            i += 1
            continue

        # Skip duplicates in arr2
        if j > 0 and arr2[j] == arr2[j - 1]:
            j += 1
            continue

        # Skip duplicates in arr3
        if k > 0 and arr3[k] == arr3[k - 1]:
            k += 1
            continue

        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1

        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return result if result else -1
