# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=0
        right=n
        while left< right:
            m=(left+right)//2
            if isBadVersion(m)==True:
                right=m
            elif isBadVersion(m)==False:
                left=m+1

        
        return left
