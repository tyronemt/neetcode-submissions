class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            l = first + 1
            r = len(nums) - 1

            while l < r:
                threesum = nums[first] + nums[l] + nums[r]

                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    ans.append([nums[first], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l+= 1
        return ans
