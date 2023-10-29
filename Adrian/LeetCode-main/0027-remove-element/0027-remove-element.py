class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for n in nums:
            if n!=val:
                nums[j] = n
                j += 1
        return j        