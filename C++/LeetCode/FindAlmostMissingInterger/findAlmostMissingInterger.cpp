// Leet code 3471. Find the Largest Almost Missing Integer

/*
You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

Return the largest almost missing integer from nums. If no such integer exists, return -1.

A subarray is a contiguous sequence of elements within an array.
 

Example 1:

Input: nums = [3,9,2,1,7], k = 3

Output: 7

Explanation:

1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
3 appears in 1 subarray of size 3: [3, 9, 2].
7 appears in 1 subarray of size 3: [2, 1, 7].
9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
We return 7 since it is the largest integer that appears in exactly one subarray of size k.

Example 2:

Input: nums = [3,9,7,2,1,7], k = 4

Output: 3

Explanation:

1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
3 appears in 1 subarray of size 4: [3, 9, 7, 2].
7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
We return 3 since it is the largest and only integer that appears in exactly one subarray of size k.

Example 3:

Input: nums = [0,0], k = 1

Output: -1

Explanation:

There is no integer that appears in only one subarray of size 1.

 

Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 50
1 <= k <= nums.length
*/

// Leet code 3471. Find the Largest Almost Missing Integer

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int largestAlmostMissingInteger(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        int n = nums.size();
        
        // Count occurrences of each number in all subarrays of size k
        for (int i = 0; i <= n - k; ++i) {
            unordered_set<int> seen;
            for (int j = i; j < i + k; ++j) {
                if (seen.find(nums[j]) == seen.end()) {
                    count[nums[j]]++;
                    seen.insert(nums[j]);
                }
            }
        }
        
        // Find the largest integer that appears in exactly one subarray of size k
        int largest = -1;
        for (const auto& entry : count) {
            if (entry.second == 1) {
                largest = max(largest, entry.first);
            }
        }
        
        return largest;
    }
};

int main() {
    Solution sol;

    // Example 1
    vector<int> nums1 = {3, 9, 2, 1, 7};
    int k1 = 3;
    cout << "Example 1 -> Expected: 7, Got: "
         << sol.largestAlmostMissingInteger(nums1, k1) << endl;

    // Example 2
    vector<int> nums2 = {3, 9, 7, 2, 1, 7};
    int k2 = 4;
    cout << "Example 2 -> Expected: 3, Got: "
         << sol.largestAlmostMissingInteger(nums2, k2) << endl;

    // Example 3
    vector<int> nums3 = {0, 0};
    int k3 = 1;
    cout << "Example 3 -> Expected: -1, Got: "
         << sol.largestAlmostMissingInteger(nums3, k3) << endl;

    return 0;
}