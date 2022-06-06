class Solution(object):
    def moveZeroes(self, nums):
        z=len(nums)
        for i in range(len(nums)-1, -1, -1):
            
            if nums[i] == 0:
                z-=1
                while i!=z:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    i+=1
            # print(nums)