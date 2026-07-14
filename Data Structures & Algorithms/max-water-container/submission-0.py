class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l = 0
        r = len(heights) - 1
        
        while l < r:
            height1 = heights[l]
            height2 = heights[r]
            smallest_heights = min(height1, height2)
            width = r - l
            area = width * smallest_heights
            most = max(most, area)

            if height1 > height2:
                r-=1
            else:
                l+=1
        return most
