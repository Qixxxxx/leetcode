#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from typing import List
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        choices = [0 for _ in range(n)]
        for i in range(n):
            choice = ["." for _ in range(n)]
            choice[i] = "Q"
            choices[i] = choice
        
        


# if __name__ == "__main__":
#     simple = Solution()
#     nums = 3
#     result = simple.solveNQueens(nums)
#     print(result)












# @lc code=end

