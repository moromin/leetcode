class Solution {
    public String reverse(String s) {
        return new StringBuilder(s).reverse().toString();
    }
    
    public String reverseWords(String s) {
        String[] strs = s.split(" ");
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < strs.length; i++) {
            if (i != 0)
                res.append(" ");
            res.append(reverse(strs[i]));
        }
        return res.toString();
    }
}