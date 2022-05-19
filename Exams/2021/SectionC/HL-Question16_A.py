# Question 16(a)
# Examination Number:

# function definition used in part (v)
def is_anagram(w1, w2):
if sorted(w1) == sorted(w2):
return True
else:
return False

word1 = input("Enter the first word: ")
word2 = "SILENT"

# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
if (sorted(word1) == sorted(word2)):
print("YES")
