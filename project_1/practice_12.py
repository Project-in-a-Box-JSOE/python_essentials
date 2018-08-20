def sqrt(x):
    if x < 0:
        raise ValueError('invalid input')
    if x == 0:
        return 0
    left = 1
    right = x
    while left <= right:
        mid = left + (right - left) // 2
        if x / mid == mid:
            return mid
        elif x / mid < mid:
            right = mid - 1
        else:
            left = mid + 1
    return right

print(sqrt(12))  # 3