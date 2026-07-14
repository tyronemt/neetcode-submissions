class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i, a in enumerate(nums):
            curr = 1
            for j,b in enumerate(nums):
                if i != j:
                    curr *= b
            ans.append(curr)
        return ans
                