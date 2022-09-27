class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        right = -1
        dominoes = [dominoes[i] for i in range(n)]
        
        for i in range(n):
            if dominoes[i] == 'L':
                if right == -1:
                    j = i - 1
                    while j >= 0 and dominoes[j] == '.':
                        dominoes[j] = 'L'
                        j -= 1
                else:
                    j, k = right + 1, i - 1
                    while j < k:
                        dominoes[j] = 'R'
                        dominoes[k] = 'L'
                        j += 1
                        k -= 1
                    right = -1
            elif dominoes[i] == 'R':
                if right != -1:
                    for j in range(right + 1, i):
                        dominoes[j] = 'R'
                right = i
        

        if right != -1:
            for j in range(right + 1, n):
                dominoes[j] = 'R'
        # print(''.join(dominoes))
        return ''.join(dominoes)
        