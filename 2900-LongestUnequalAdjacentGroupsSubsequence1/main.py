class Solution:
    def getLongestSubsequence(self, words, groups):
        result_subsequence = []
        if not words:
            return []
        result_subsequence.append(words[0])
        last_added_group_value = groups[0]
        
        for i in range(1, len(words)):
            current_group_value = groups[i]
            if current_group_value != last_added_group_value:
                result_subsequence.append(words[i])
                last_added_group_value = current_group_value
                
        return result_subsequence
        
        