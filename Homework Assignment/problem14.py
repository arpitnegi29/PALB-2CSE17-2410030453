def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums1 = [1, 3, 4, 2, 2]
print("Duplicate number:", find_duplicate(nums1)) 

nums2 = [3, 1, 3, 4, 2]
print("Duplicate number:", find_duplicate(nums2)) 
