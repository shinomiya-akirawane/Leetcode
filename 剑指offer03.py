import copy
def findRepeatNumber(nums: list[int]) -> int:
    for num in nums:
        temp = copy.deepcopy(nums)
        temp.remove(num)
        if num in temp:
            return num

findRepeatNumber([0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])