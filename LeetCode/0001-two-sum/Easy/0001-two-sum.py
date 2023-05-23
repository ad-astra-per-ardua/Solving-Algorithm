class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for index, num in enumerate(nums):
            if num in diff_dict:
                return [diff_dict[num], index]
            diff_dict[target - num] = index
        print(two_sum(nums1, target1))