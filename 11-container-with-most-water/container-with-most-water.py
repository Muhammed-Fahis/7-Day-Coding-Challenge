class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        l =0 
        r = len(height) - 1

        while l < r:
            maximum = max(maximum,(r - l)* min(height[r],height[l]))
            if height[l] > height[r]:
                # area = height[r] * (r - l)
                r -= 1
            else:
                # area = height[l] * (r - l)
                l += 1
                
            # maximum = max(maximum,area)
        return maximum
