def msort(m):
    if len(m) == 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    left = msort(left)
    right = msort(right)
    return merge(left, right)


def merge(left, right):
    result = [0] * (len(left) + len(right))
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result[i+j] = left[i]
            i += 1
        else:
            result[i+j] = right[j]
            j += 1
    while i < len(left):
        result[i+j] = left[i]
        i += 1
    while j < len(right):
        result[i+j] = right[j]
        j += 1
    return result


m = list(map(int, input().split()))
ans = msort(m)
print(ans[500000])