class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def solve(index, current_xor):

            if index == len(nums):
                return current_xor
            

            pick = solve(index + 1, current_xor ^ nums[index])
            

            not_pick = solve(index + 1, current_xor)
            

            return pick + not_pick
            
        return solve(0, 0)