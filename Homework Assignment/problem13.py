def min_jumps(arr):
    n = len(arr)
    if n == 0 or arr[0] == 0:
        return -1

    jumps = 0        
    farthest = 0     
    current_end = 0  

    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

            if current_end >= n - 1:
                break

        if i >= farthest:
            return -1  

    return jumps if current_end >= n - 1 else -1


arr1 = [2, 3, 1, 1, 4]
print("Minimum jumps:", min_jumps(arr1)) 

arr2 = [1, 0, 2, 3]
print("Minimum jumps:", min_jumps(arr2))  
