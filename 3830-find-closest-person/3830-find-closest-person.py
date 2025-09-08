class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if max(x,z)-min(x,z)==max(y,z)-min(y,z):
            return 0
        elif max(x,z)-min(x,z)<max(y,z)-min(y,z):
            return 1
        else:
            return 2

        