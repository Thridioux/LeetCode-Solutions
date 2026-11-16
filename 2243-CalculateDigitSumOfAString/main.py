class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            chunks = []
            for i in range(0, len(s), k):
                chunk = s[i : i + k]
                digit_sum = sum(int(d) for d in chunk)
                chunks.append(str(digit_sum))
            s = "".join(chunks)
        return s