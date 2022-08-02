def removeDuplicates( nums: list[int]) -> int:
    print(id(nums))
    nums[:] = list(set(nums))
    print(id(nums))
    return nums

print(removeDuplicates([1,1,2]))