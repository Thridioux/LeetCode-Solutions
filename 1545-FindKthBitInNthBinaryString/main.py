class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        lenght = 2**n - 1
        invert = False
        
        while lenght > 1:
            half = lenght // 2
            if k<=half:
                lenght = half
                
            elif k > half + 1:
                k = lenght - k + 1
                lenght = half
                invert = not invert
            else:
                return '1' if not invert else '0'
        return '1' if invert else '0'