class Solution(object):
    def partitionArray(self, nums, k):
        nums.sort()
        l = len(nums)
        res = 1
        
        min_val = nums[0]
        max_val = min_val + k

        for i in range(len(nums)):
            if nums[i] <= max_val:
                continue
            else:
                res+=1
                min_val = nums[i]
                max_val = min_val +k

        return res

        
                
x = Solution()
print(x.partitionArray([2,2,5,4],0))
        