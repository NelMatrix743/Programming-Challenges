class Solution:

    def divideArray(self, nums: List[int]) -> bool:
        nums.sort() # O(n logn)
        pair_counter: int = len(nums) // 2
        for idx in range(0, len(nums), 2): # O(n)
            if nums[idx] == nums[idx + 1]:
                pair_counter -= 1
        return pair_counter == 0

# Time complexity: O((nlogn) + n); This does not look good, I know
# Expect some optimization in the future ;)
# eosc