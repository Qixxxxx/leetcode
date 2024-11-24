#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # # 暴力递归
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)

        # dp
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp_list = [0 for i in range(n + 1)]
        dp_list[1] = dp_list[2] = 1
        for i in range(n + 1):
            if i >= 3 :
                dp_list[i] = dp_list[i - 1] + dp_list[i - 2]
        return dp_list[n]



# if __name__ == "__main__":
#     simple = Solution()
#     n = 3
#     result = simple.fib(n)
#     print(result)

# @lc code=end

