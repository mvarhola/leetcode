class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            remainder = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == remainder:
                    return [i,j]