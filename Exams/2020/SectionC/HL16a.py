# Question 16(a)
# Examination Number:

# Prompt the user to enter a password and store the value entered in the variable password
password = input("Enter a password: ")

# A variable to store all the lowercase letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

# The variables lowercase and uppercase indicate the presence or absence of lowercase and uppercase characters in the password
lowercase = False  # True if password contains a lowercase letter
uppercase = False  # True if password contains an uppercase letter

# Loop through each character in the password and check the password for specific characters
for character in password:
    if character in LOWER_CASE_LETTERS:
        lowercase = True
    if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppercase = True

# Calculate the score based on the rules
score = 0

# Rule 1
if len(password) > 7:
    score = score + 5

# Rule 2
if lowercase:
    score = score + 1

# Rule 3
if lowercase and uppercase:
    score = score + 5

# Display the score
print(score)
