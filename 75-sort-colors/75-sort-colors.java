class Solution {
    
    void swap(int[] nums, int i, int j) {
        int tmp;
        
        tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    
    // void printArray(int[] nums) {
    //     System.out.print("[");
    //     for (int num: nums) {
    //         System.out.print(num + ",");
    //     }
    //     System.out.println("]");
    // }
    
    public void sortColors(int[] nums) {
        int start = 0, mid = 0, end = nums.length - 1;
        int pivot = 1;
        
        while (mid <= end) {
            if (nums[mid] < pivot) {
                swap(nums, start, mid);
                start++;
                mid++;
            } else if (nums[mid] > pivot) {
                swap(nums, mid, end);
                end--;
            } else {
                mid++;
            }
            // printArray(nums);
        }
    }
}