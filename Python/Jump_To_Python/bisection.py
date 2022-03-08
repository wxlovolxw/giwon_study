import math
import bisect


def numSubarrayProductLessThanK(nums, k):
    if k == 0: return 0
    k = math.log(k)

    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + math.log(x))

    ans = 0
    for i, x in enumerate(prefix):
        j = bisect.bisect(prefix, x+k-1e-9, i+1)
        ans += j - i -1
    return ans

nums = [10, 5, 2, 6]
k = 100

print(numSubarrayProductLessThanK(nums,k))