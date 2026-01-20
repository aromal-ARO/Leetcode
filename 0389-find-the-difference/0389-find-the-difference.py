class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_t = 0
        sum_s =0
        for i in s:
            sum_s += ord(i)
        for i in t:
            sum_t += ord(i)
        diff = sum_t - sum_s
        return chr(diff)