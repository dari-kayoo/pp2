
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        x = 0
        maxi = 0
        for i in range(len(gain)):
            x += gain[i]
            if x > maxi:
                maxi = x
        return maxi
