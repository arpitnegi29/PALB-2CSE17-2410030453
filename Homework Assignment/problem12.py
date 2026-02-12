def minimize_height_difference(arr, k):
    n = len(arr)
    if n == 1:
        return 0

    arr.sort()
    ans = arr[-1] - arr[0]  # initial difference

    smallest = arr[0] + k
    largest = arr[-1] - k

    for i in range(1, n - 1):
        subtract = arr[i] - k
        add = arr[i] + k

        if subtract >= smallest or add <= largest:
            continue

        if largest - subtract <= add - smallest:
            smallest = subtract
        else:
            largest = add

    return min(ans, largest - smallest)


arr1 = [1, 5, 8, 10]
k1 = 2
print("Minimum difference:", minimize_height_difference(arr1, k1)) 

arr2 = [3, 9, 12, 16, 20]
k2 = 3
print("Minimum difference:", minimize_height_difference(arr2, k2)) 
