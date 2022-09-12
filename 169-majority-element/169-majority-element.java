class Solution {
    public int majorityElement(int[] nums) {
        int votes = 0, candidate = nums[0];
        for (int num: nums) {
            if (votes == 0) {
                candidate = num;
                votes++;
            } else if (num == candidate) {
                votes++;
            } else {
                votes--;
            }
        }
        return candidate;
    }
}