def singleNumber(nums: list[int]) -> int:
    nums[:] = sorted(nums)
    temp = '0'
    for num in nums:
        if temp == '0':
            temp = num
        elif temp == num:
            temp = '0'
        else:
            continue
    return temp

singleNumber([1,0,1])