class Solution:
    def checkString(self, s: str) -> bool:
        # Every 'a' appears before every 'b' if and only if
        # there is no 'b' immediately followed by an 'a' anywhere in the string.
        return "ba" not in s
