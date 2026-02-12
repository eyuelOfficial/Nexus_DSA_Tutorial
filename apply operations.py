class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

      
        ans = []
        counter = 0

        for num in nums:
            if num != 0:
                ans.append(num)
                counter += 1

        while counter < len(nums):
            ans.append(0)
            counter += 1

        return ans
