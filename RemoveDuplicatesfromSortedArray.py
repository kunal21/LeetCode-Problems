class Solution:
    def removeDuplicates(self, nums):
        if len(nums) != 0:
            compare = nums[0]
        else:
            return 0
        length = 1
        for i in nums[1:]:
            if compare == i:
                nums.pop(nums.index(i))
                pass
            else:
                length = length + 1
                compare = i
            
        return length