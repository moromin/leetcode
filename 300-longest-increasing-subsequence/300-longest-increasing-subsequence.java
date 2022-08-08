import java.util.*;

class Solution {
    public int bisectLeft(List<Integer> list, int target) {
        if (list == null) {
            return -1;
        }
        
        int left = 0, right = list.size() - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            
            if (list.get(mid) == target) {
                return mid;
            } else if (list.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return left;
    }
    
    public int lengthOfLIS(int[] nums) {
        List<Integer> dp = new ArrayList<>();
        
        dp.add(nums[0]);
        for (int num: nums) {
            if (dp.get(dp.size() - 1) < num) {
                dp.add(num);
            } else {
                dp.set(bisectLeft(dp, num), num);
            }
        }
        
        for (Integer v: dp) {
            System.out.println(v);
        }
        return dp.size();
    }
}