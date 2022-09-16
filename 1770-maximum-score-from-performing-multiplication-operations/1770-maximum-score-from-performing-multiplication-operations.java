class Solution {
    int n;
    int m;
    int[][] dp;
    int[] nums;
    int[] multipliers;
    
    public int maximumScore(int[] nums, int[] multipliers) {
        this.n = nums.length;
        this.m = multipliers.length;
        this.dp = new int[m][m];
        this.nums = nums;
        this.multipliers = multipliers;
        return dfs(0, 0);
    }
    
    private int dfs(int l, int i) {
        if (i >= m)
            return 0;
        if (dp[l][i] == 0) {
            int r = n - 1 - (i - l);
            dp[l][i] = Math.max(
                nums[l] * multipliers[i] + dfs(l+1, i+1),
                nums[r] * multipliers[i] + dfs(l, i+1));
        }
        // System.out.println(l + ", " +  i + ", " + dp[l][i]);
        return dp[l][i];
    }
}