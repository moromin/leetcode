class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int sum = 0;
        for (int num: nums) {
            if (num % 2 == 0)
                sum += num;
        }
        
        int n = nums.length;
        int[] res = new int[n];
        
        for (int i = 0; i < n; i++) {
            int val = queries[i][0], idx = queries[i][1];
            if (nums[idx] % 2 == 0)
                sum -= nums[idx];
            nums[idx] += val;
            if (nums[idx] % 2 == 0)
                sum += nums[idx];
            res[i] = sum;
        }
        
        return res;
    }
}