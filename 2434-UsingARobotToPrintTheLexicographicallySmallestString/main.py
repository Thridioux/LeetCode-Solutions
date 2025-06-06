class Solution:
    def robotWithString(self, s: str) -> str:
            char_counts = [0] * 26
            for char_code in map(ord, s):
                char_counts[char_code - ord('a')] += 1
                
            min_char_in_s_ord = ord('a')

            while min_char_in_s_ord < ord('z') and char_counts[min_char_in_s_ord - ord('a')] == 0:
                min_char_in_s_ord += 1
            
            stack_t = []
            result_p = []
            
            for current_char_from_s in s:
                stack_t.append(current_char_from_s)
                char_counts[ord(current_char_from_s) - ord('a')] -= 1
                
                while min_char_in_s_ord <= ord('z') and char_counts[min_char_in_s_ord - ord('a')] == 0:
                    min_char_in_s_ord += 1

                min_s_char_to_compare = chr(min_char_in_s_ord) if min_char_in_s_ord <= ord('z') else '{'
                
                while stack_t and stack_t[-1] <= min_s_char_to_compare:
                    result_p.append(stack_t.pop())

            while stack_t:
                result_p.append(stack_t.pop())
            
            return ''.join(result_p)