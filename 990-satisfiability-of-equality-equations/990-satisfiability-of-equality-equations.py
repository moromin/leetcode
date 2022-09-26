class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = dict()
        
        def find(x):
            if x not in parents:
                return x
            else:
                return find(parents[x])
        
        for eq in equations:
            if eq[1] == '=':
                a = find(eq[0])
                b = find(eq[3])
                if a != b:
                    parents[b] = a
        # print(parents)
        
        for eq in equations:
            if eq[1] == '!' and find(eq[0]) == find(eq[3]):
                return False
        return True