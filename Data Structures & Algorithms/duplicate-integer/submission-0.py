class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        clean: dict = {}

        for i,x in enumerate(nums):
            clean[x] = i;

        return True if len(clean) != len(nums) else False

            