#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from typing import List


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        checkboard: List = [["."] * n for _ in range(n)]

        def backtrack(row):
            n = len(checkboard)
            # 如果到最后一行了，则将结果添加到result里
            if row == n:
                tmp = ["".join(i) for i in checkboard]
                result.append(tmp)
                return

            for col in range(n):
                if not is_valid(checkboard, row, col):
                    continue
                checkboard[row][col] = "Q"
                if backtrack(row + 1):
                    return True
                checkboard[row][col] = "."
            return False

        backtrack(0)
        return result


def is_valid(checkboard: List[List[str]], row: int, col: int):
    n = len(checkboard)
    # 查看上方是否有Q
    for i in range(row):
        if checkboard[i][col] == "Q":
            return False

    # 查看右上方是否有Q
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
        if checkboard[i][j] == "Q":
            return False

    # 查看左上方是否有Q
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if checkboard[i][j] == "Q":
            return False

    return True


# if __name__ == "__main__":
#     simple = Solution()
#     nums = 4
#     result = simple.solveNQueens(nums)
#     print(result)


# @lc code=end
