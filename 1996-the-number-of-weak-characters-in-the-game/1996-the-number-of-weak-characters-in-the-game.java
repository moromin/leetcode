import java.util.*;

class Solution {
    
    public int numberOfWeakCharacters(int[][] properties) {
        if (properties == null || properties[0] == null) {
            return 0;
        }
        
        Arrays.sort(properties, (a, b) -> a[0] != b[0] ? a[0] - b[0] : b[1] - a[1]);
        
        int res = 0;
        Stack<Integer> stack = new Stack<>();
        for (int[] p: properties) {
            int atk = p[0], def = p[1];
            while (!stack.isEmpty() && stack.peek() < def) {
                stack.pop();
                res++;
            }
            stack.push(def);
        }
        
        return res;
    }
}