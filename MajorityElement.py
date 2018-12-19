class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        visited = []
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            if nums[i] in visited:
                pass
            else:
                visited.append(nums[i])
                for j in range((i+1),len(nums)):
                    if nums[i] == nums[j]:
                        counter += 1 
                        if(counter > (math.floor(len(nums)/2))):
                            return nums[j]
                            break
            counter = 1