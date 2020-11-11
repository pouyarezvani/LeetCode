def runningSum(nums):
    sum = 0
    new_arr = []
    for i in nums:
        sum += i
        new_arr.append(sum)

    return new_arr


arr = [1, 2, 3, 4]
print(runningSum(arr))
