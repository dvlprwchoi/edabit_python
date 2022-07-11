def findLargestNum(nums):
    return max(nums)


def findLargestNum(nums):
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    return largest


def findLargestNum(nums):
    return sorted(nums)[-1]
