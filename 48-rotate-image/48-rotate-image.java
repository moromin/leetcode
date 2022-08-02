class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        
        int start = 1;
        for (int i = 0; i < n - 1; i++) {
            for (int j = start; j < m; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
            start++;
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m/2; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][m - 1 - j];
                matrix[i][m - 1 - j] = tmp;
            }
        }
    }
}