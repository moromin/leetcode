class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        s = set()
        for word in words:
            tmp = ""
            for i in range(len(word)):
                tmp += MORSE[ord(word[i]) - ord('a')]
            s.add(tmp)
        
        return len(s)
        
        