import java.util.*;

class Solution {
    public int combinationSum4(int[] nums, int target) {
        Integer[] dp = new Integer[target+1];
        
        dp[0] = 1;
        for (int i = 0; i < target; i++) {
            if (dp[i] == null)
                continue;
            for (int num: nums)
            {
                if (i + num <= target) {
                    if (dp[i + num] == null)
                        dp[i + num] = 0;
                    dp[i + num] += dp[i];
                }
            }        
        }
        
        return dp[target] != null ? dp[target] : 0;
    }
}