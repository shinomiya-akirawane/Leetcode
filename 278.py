def isBadVersion(n):
    if n == 4 or n == 5:
        return True
    else:
        return False
def firstBadVersion(n: int) -> int:
    l = 1
    r = n
    while l <= r:
        mid = int((l + r)//2)
        if isBadVersion(mid) == True:
            if isBadVersion(mid-1) == False:
                return mid
            else:
                r = mid
        else:
            l = mid

print(firstBadVersion(5))