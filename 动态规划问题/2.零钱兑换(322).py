#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
from typing import List

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # 暴力解
        # def deal(n: int) -> int:
        #     if n == 0:
        #         return 0
        #     if n < 0:
        #         return -1
        #     res = float("INF")
        #     for coin in coins:
        #         sub_problem_result = deal(n - coin)
        #         if sub_problem_result == -1 :
        #             continue
        #         res = min(res, 1 + sub_problem_result)
        #     return res if res != float("INF") else -1
        
        # return deal(amount)
        dp_list = [amount + 1 for i in range(amount + 1)]
        dp_list[0] = 0
        for i in range(len(dp_list)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp_list[i] = min(dp_list[i], 1 + dp_list[i - coin])
        return -1 if (dp_list[amount] == amount + 1) else dp_list[amount]


# if __name__ == "__main__":
#     simple = Solution()
#     coins = [1,2,5]
#     n = 11
#     result = simple.coinChange(coins, n)
#     print(result)

        
# @lc code=end

