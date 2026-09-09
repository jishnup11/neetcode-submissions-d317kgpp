class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        size = len(nums)
        out = [0] * size
        zer_cnt = 0
        for i in range(size):
            if nums[i] ==0:
                zer_cnt += 1
            else:
                product *= nums[i]
        if zer_cnt > 1:
            return out
        elif zer_cnt == 1:
            for i in range(size):
                if nums[i] == 0:
                    out[i] = product
                else:
                    out[i] = 0
            return out
        else:
            for i in range(size):
                out[i] = int(product / nums[i])
            return out


        
