class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int rounds = minutesToTest / minutesToDie;
        int pigs = 0;
        int N = 1;
        
        while (N < buckets)
        {
            N *= (rounds + 1);
            pigs++;   
        }
        return pigs;
    }
}