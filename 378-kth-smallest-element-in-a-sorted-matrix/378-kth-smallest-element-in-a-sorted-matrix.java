class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        
        int low = matrix[0][0], high = matrix[n - 1][n - 1];
        int row = n, col = n;
        
        while (low <= high) {
            int mid = (low + high) / 2;
            int count = 0;
            int maxNum = low;
            
            for (int r = 0, c = col - 1; r < row; r++) {
                while (c >= 0 && matrix[r][c] > mid)
                    c--;
                if (c >= 0) {
                    count += (c + 1);
                    maxNum = Math.max(maxNum, matrix[r][c]);
                } else {
                    break;
                }
            }
            
            if (count == k)
                return maxNum;
            else if (count < k)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return low;
    }
}