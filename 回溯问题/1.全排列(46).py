#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(track, nums):
            if len(track) == len(nums):
                result.append(track.copy())
                return
            for i in nums:
                if i in track:
                    continue
                track.append(i)
                dfs(track, nums)
                track.pop()

        dfs([], nums)
        return result

# if __name__ == "__main__":
#     simple = Solution()
#     nums = [1,2,3]
#     result = simple.permute(nums)
#     print(result)
            
        
# @lc code=end