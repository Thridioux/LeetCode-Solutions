word = "abacabadabacaba"
pushes = {"one_push": word[0]}
distinct_char = 1
for i in range(1, len(word)):
    if distinct_char < 8:
        pushes["one_push"] = word[i]
        distinct_char += 1
    else:
        pushes["two_pushes"] = word[i]
print(pushes)
