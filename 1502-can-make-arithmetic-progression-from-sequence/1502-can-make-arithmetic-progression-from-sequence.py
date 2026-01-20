class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        new = sorted(arr)
        diff = new[1]-new[0]
        
        for i in range(len(new)-1):
            if (new[i+1]-new[i]) != diff:
                return False
        else:
            return True
        