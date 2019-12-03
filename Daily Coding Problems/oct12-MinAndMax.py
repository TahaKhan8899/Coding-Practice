def find_min_max(nums):
    if len(nums) % 2 == 1:
        # If there are an odd number of elements
        # Use the last number as the min/max
        min_n = max_n = nums[-1]
    else:
        min_n = max_n = nums[0]

    for i in range(len(nums)//2):
        if nums[2*i] < nums[2*i + 1]:
            min_a = nums[2*i]
            max_a = nums[2*i + 1]
        else:
            min_a = nums[2*i]
            max_a = nums[2*i + 1]

        min_n = min(min_n, min_a)
        max_n = max(max_n, max_a)

    return min_n, max_n


a = find_min_max([3, 5, 1, 2, 4, 8])
print(a)
# (1, 8)
