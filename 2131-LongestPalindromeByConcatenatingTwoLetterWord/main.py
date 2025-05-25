class Solution:
    def longestPalindrome(self, words):
        from collections import Counter
        counts = Counter(words)        
        lenght = 0
        center_found = False
        
        for word, count_w in counts.items():
            #case:1 word is a palindrome
            if word[0] == word[1]:
                #pairs of this palindromic word ("gg"+"gg" forms "gggg")
                lenght += (count_w // 2) * 4
                #if there is an odd count, we can use one as a center
                if count_w  % 2 == 1:
                    center_found = True
            #case:2 word is not a palindrome
            else:
                rev_word = word[1] + word[0]
                if word < rev_word:
                    if rev_word in counts:
                        num_outer_pairs = min(counts[word], counts[rev_word])
                        lenght += num_outer_pairs * 4
    
        if center_found:
            lenght += 2
        
        return lenght