import java.util.*;

class Solution {
    void print2dArray(int[][] arr2d) {
        for (int[] arr: arr2d) {
            for (int elem: arr) {
                System.out.print(elem + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
    
    public int numberOfWeakCharacters(int[][] properties) {
        if (properties == null || properties[0] == null) {
            return 0;
        }
        
        // this.print2dArray(properties);
        Arrays.sort(properties, (a, b) -> a[0] != b[0] ? a[0] - b[0] : b[1] - a[1]);
        // this.print2dArray(properties);
        
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