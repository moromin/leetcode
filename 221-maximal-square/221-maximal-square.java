class Solution {
    
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int result = 0;

        int[][] dp = new int[m+1][n+1];
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (matrix[i-1][j-1] == '1') {
                    dp[i][j] = Math.min(Math.min(dp[i][j-1], dp[i-1][j-1]), dp[i-1][j]) + 1;
                    result = Math.max(dp[i][j], result);
                }
            }
        }
        
        // System.out.println("matrix");
        // for (int i = 0; i < m; i++) {
        //     for (int j = 0; j < n; j++) {
        //         System.out.print(matrix[i][j] + " ");
        //     }
        //     System.out.println();
        // }
        // System.out.println("\ndp");
        // for (int i = 0; i < m; i++) {
        //     for (int j = 0; j < n; j++) {
        //         System.out.print(dp[i+1][j+1] + " ");
        //     }
        //     System.out.println();
        // }
        
        return result * result;
    }
}