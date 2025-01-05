class Solution:
    def shiftingLetters(self, s: str, shifts):
        prefix_diff = [0] * (len(s) + 1)
        
        for left, right, d in shifts:
            prefix_diff[right + 1] += 1 if d >0 else -1
            prefix_diff[left] += -1 if d>0 else 1
            
        diff = 0
        res = [ord(c)- ord('a') for c in s]
        
        for i in reversed(range(len(prefix_diff))):
            diff += prefix_diff[i]
            res[i-1] = (res[i-1] + diff) % 26
        
        s = [chr(c + ord('a')) for c in res]
        return ''.join(s)
        