class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] == nums[j]:
                    res += 1
        return res 