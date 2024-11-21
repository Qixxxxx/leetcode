#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 双指针
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # 使用哈希表存储，用空间换时间
        index_map = {}
        for index, value in enumerate(nums):
            other_value = target - value
            if (other_value in index_map.keys()):
                return [index, index_map[other_value]]
            index_map[value]=index
        
# @lc code=end