class Solution:
    def guessNumber(self, n: int) -> int:
        s=0
        e=n
        while s<=e:
            mid=(s+e)//2
            result=guess(mid)
            if result==0:
                return mid
            elif result==-1:
                e=mid-1
            elif result==1:
                s=mid+1

            