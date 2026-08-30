# Python/LeetCode/recursions/recursions.py

def recurse(nums):
    if nums == 0:
        return
    print("foo" + str(nums))   # runs before the recursive call (going down)
    recurse(nums - 1)
    print("bar" + str(nums))   # runs after the recursive call returns (coming back up)\

recurse(3)


        



