
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=list(map(lambda x: x**2,nums))
        left=0
        right=len(s)-1
        a=[]
        while left<=right:
            if(s[left]<s[right]):
                a.append(s[right])
                right-=1
            else:
                a.append(s[left])
                left+=1

            

        a.reverse()
        
        return a
        