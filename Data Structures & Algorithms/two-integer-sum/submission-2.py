class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val: dict = {nums[0]:0}
        for i in range(1,len(nums)):
            if (j:= val.get(target - nums[i],-1)) != -1:
                return [j,i]
            val[nums[i]] =i
        return [0,0]



        