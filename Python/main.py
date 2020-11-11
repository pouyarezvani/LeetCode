# A list of my python challenges.

def runningSum(nums):
    sum = 0
    new_arr = []
    for i in nums:
        sum += i
        new_arr.append(sum)

    return new_arr


arr = [1, 2, 3, 4]
# print(runningSum(arr))


def reverseNum(num):
    num_list = [int(d) for d in str(num)]
    reverse_list = num_list[::-1]

    # Loop over the reverse_list and print print each i on the same line with end=""
    print("this is the result of forloop")
    for i in reverse_list:
        print(i, end="")

    print("\n")
    # This one liner turns a list of nums to single integer.
    # we can return it below.
    print("this is the result of no print with return")
    num = int(''.join(map(str, reverse_list)))

    return num


print(reverseNum(123))
