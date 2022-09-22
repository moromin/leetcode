class Solution {
    
    public String reverseWords(String s) {
        String[] strs = s.split(" ");
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < strs.length; i++) {
            if (i != 0)
                res.append(" ");
            res.append(new StringBuilder(strs[i]).reverse().toString());
        }
        return res.toString();
    }
}