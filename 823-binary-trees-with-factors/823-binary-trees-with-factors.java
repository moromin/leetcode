import java.util.*;

class Solution {    
    public int numFactoredBinaryTrees(int[] arr) {
        Arrays.sort(arr);
        long res = 0L;
        long MOD = (long)1e9 + 7;
        HashMap<Integer, Long> dp = new HashMap<>();
        
        for (int i = 0; i < arr.length; i++) {
            dp.put(arr[i], 1L);
            for (int j = 0; j < i; j++) {
                if (arr[i] % arr[j] == 0)
                    dp.put(arr[i], (dp.get(arr[i]) + dp.get(arr[j]) * dp.getOrDefault(arr[i] / arr[j], 0L) % MOD));
            }
            res = (res + dp.get(arr[i])) % MOD;
        }
        
        
        return (int)res;
    }
}