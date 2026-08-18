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

int largestAlmostMissingInteger(List<int> nums, int k) {
  Map<int, int> count = {};
  int n = nums.length;

  // For each subarray of size k, count each distinct value once
  for (int i = 0; i <= n - k; i++) {
    Set<int> seen = {};
    for (int j = i; j < i + k; j++) {
      int val = nums[j];
      if (!seen.contains(val)) {
        count[val] = (count[val] ?? 0) + 1;
        seen.add(val);
      }
    }
  }

  // Find the largest value that appears in exactly one subarray
  int largest = -1;
  count.forEach((val, occurrences) {
    if (occurrences == 1 && val > largest) {
      largest = val;
    }
  });

  return largest;
}

void main() {
  // Example 1
  List<int> nums1 = [3, 9, 2, 1, 7];
  int k1 = 3;
  print("Example 1 -> Expected: 7, Got: ${largestAlmostMissingInteger(nums1, k1)}");

  // Example 2
  List<int> nums2 = [3, 9, 7, 2, 1, 7];
  int k2 = 4;
  print("Example 2 -> Expected: 3, Got: ${largestAlmostMissingInteger(nums2, k2)}");

  // Example 3
  List<int> nums3 = [0, 0];
  int k3 = 1;
  print("Example 3 -> Expected: -1, Got: ${largestAlmostMissingInteger(nums3, k3)}");
}