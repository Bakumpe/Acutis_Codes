# Acutis_Codes/Python/LeetCode/containerWithMostWater.py

# condtainer with max area
def maxArea(height):
    left, right = 0, len(height) - 1
    maxWater = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        maxWater = max(maxWater, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxWater

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(heights))

# container with min area
def minArea(height):
    return min(min(height[i], height[i+1]) for i in range(len(height) - 1))

heights = [6, 4, 8, 1, 5, 9, 8, 3, 7]
print(minArea(heights)) 


