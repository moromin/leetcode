class Solution {
    
    public int maximalSquare(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        int result = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0){
                    if (matrix[i][j] == '1' && result == 0) {
                        result = 1;   
                    }
                } else if (matrix[i][j] == '1') {
                    int cur = Math.min(Math.min(matrix[i][j-1], matrix[i-1][j-1]), matrix[i-1][j]) - '0' + 1;
                    matrix[i][j] = (char)(cur + '0');
                    result = Math.max(cur, result);
                }
            }
        }
        
        return result * result;
    }
}