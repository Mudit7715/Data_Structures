class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashmap and hashmap[val] !=i:
                return [i,hashmap[val]]

        return []
