class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # create a dictionary to store the anagrams
        anagrams = {}
        # iterate over the list of strings
        for string in strs:
                
            sorted_string = ''.join(sorted(string))
            # if the sorted string is already in the dictionary
            if sorted_string in anagrams:
                # append the string to the list of anagrams
                anagrams[sorted_string].append(string)
            else:
                # create a new key in the dictionary
                anagrams[sorted_string] = [string]
            
        return list(anagrams.values())    
    
    
# test the solution
s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["eat","tea","ate"],["tan","nat"],["bat"]]