import java.util.*;

class Solution {
    
    public int numberOfWeakCharacters(int[][] properties) {
        Arrays.sort(properties, (a, b) -> a[0] == b[0] ? Integer.compare(b[1], a[1]) : Integer.compare(a[0], b[0]));
        
        int res = 0;
        int len = properties.length;
        
        int maxDef = properties[len-1][1];
        
        for (int i = len-2; i >= 0; i--) {
            if (properties[i][1] < maxDef) {
                res++;
            } else {
                maxDef = properties[i][1];
            }
        }
        return res;
    }
}