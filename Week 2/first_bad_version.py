# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version == 5

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1 
        
        low = 1
        high = n

        while low <= high:

            mid = (low + high)// 2

            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low