// Leet code 3471. Find the Largest Almost Missing Integer

/*
You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

Return the largest almost missing integer from nums. If no such integer exists, return -1.

Constraints:
1 <= nums.length <= 50
0 <= nums[i] <= 50
1 <= k <= nums.length
*/

#include <stdio.h>

#define MAX_VAL 51   // values range 0..50, so 51 possible values

int largestAlmostMissingInteger(int nums[], int n, int k) {
    int count[MAX_VAL] = {0};   // count[x] = number of size-k subarrays x appears in

    // For each subarray of size k, count each distinct value once
    for (int i = 0; i <= n - k; ++i) {
        int seen[MAX_VAL] = {0};   // tracks whether value already counted for this subarray
        for (int j = i; j < i + k; ++j) {
            int val = nums[j];
            if (!seen[val]) {
                count[val]++;
                seen[val] = 1;
            }
        }
    }

    // Find the largest value that appears in exactly one subarray
    int largest = -1;
    for (int val = 0; val < MAX_VAL; ++val) {
        if (count[val] == 1 && val > largest) {
            largest = val;
        }
    }

    return largest;
}

int main() {
    // Example 1
    int nums1[] = {3, 9, 2, 1, 7};
    int k1 = 3;
    printf("Example 1 -> Expected: 7, Got: %d\n",
           largestAlmostMissingInteger(nums1, 5, k1));

    // Example 2
    int nums2[] = {3, 9, 7, 2, 1, 7};
    int k2 = 4;
    printf("Example 2 -> Expected: 3, Got: %d\n",
           largestAlmostMissingInteger(nums2, 6, k2));

    // Example 3
    int nums3[] = {0, 0};
    int k3 = 1;
    printf("Example 3 -> Expected: -1, Got: %d\n",
           largestAlmostMissingInteger(nums3, 2, k3));

    return 0;
}