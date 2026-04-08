class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashl = {}
        res = []
        for i in range(len(nums)):
            hashl[nums[i]]=i
        for i in range(len(nums)):
            second_num = target - nums[i]
            if (second_num in hashl) and (hashl[second_num]!=i):
                return [i,hashl[second_num]]

                   

            
        