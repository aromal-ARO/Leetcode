class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        is_arthmatic = True

        for i in range(2,len(arr)):
            if arr[i] - arr[i-1] != diff:
                is_arthmatic = False
        return is_arthmatic