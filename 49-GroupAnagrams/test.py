# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# for string in strs:
#     sorted_string = ''.join(sorted(string))
#     print(sorted_string)

def has_unique_chars(string):
    char_set = set() # set to store the characters
    for char in string:
        if char in char_set:
            return False
        char_set.add(char)
    return True

print(has_unique_chars("hello"))  # False
    
