class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize an array to store the number of ways for each step
        dp = [0] * (n + 1)

        # There's one way to reach the first step
        dp[1] = 1
        # There are two ways to reach the second step: (1, 1) or (2)
        dp[2] = 2

        # Calculate the number of ways for each step
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
