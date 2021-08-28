class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid[0]); n=len(obstacleGrid)
        dp= [[0]*(m+1) for _ in range(n+1)] 
        
        dp[0][1]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if obstacleGrid[i-1][j-1]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                                              
        return dp[n][m]