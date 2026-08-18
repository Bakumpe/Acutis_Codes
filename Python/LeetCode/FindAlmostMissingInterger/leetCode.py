# Leet code 3471. Find the Largest Almost Missing Integer

"""
You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

Return the largest almost missing integer from nums. If no such integer exists, return -1.

Constraints:
1 <= nums.length <= 50
0 <= nums[i] <= 50
1 <= k <= nums.length
"""

from typing import List


class Solution:
    def largestAlmostMissingInteger(self, nums: List[int], k: int) -> int:
        count = {}
        n = len(nums)

        # For each subarray of size k, count each distinct value once
        for i in range(0, n - k + 1):
            seen = set()
            for j in range(i, i + k):
                val = nums[j]
                if val not in seen:
                    count[val] = count.get(val, 0) + 1
                    seen.add(val)

        # Find the largest value that appears in exactly one subarray
        largest = -1
        for val, occurrences in count.items():
            if occurrences == 1 and val > largest:
                largest = val

        return largest


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [3, 9, 2, 1, 7]
    k1 = 3
    print(f"Example 1 -> Expected: 7, Got: {sol.largestAlmostMissingInteger(nums1, k1)}")

    # Example 2
    nums2 = [3, 9, 7, 2, 1, 7]
    k2 = 4
    print(f"Example 2 -> Expected: 3, Got: {sol.largestAlmostMissingInteger(nums2, k2)}")

    # Example 3
    nums3 = [0, 0]
    k3 = 1
    print(f"Example 3 -> Expected: -1, Got: {sol.largestAlmostMissingInteger(nums3, k3)}")

    