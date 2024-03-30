n = int(input())
for i in range(n):
    k = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    j = 1
    while j < len(nums):
        if nums[j] - nums[j-1] == 0 or nums[j] - nums[j-1] == 1:
            nums.pop(j-1)
        else:
            j += 1

    if len(nums) == 1:
        print("YES")
    else:
        print("NO")
