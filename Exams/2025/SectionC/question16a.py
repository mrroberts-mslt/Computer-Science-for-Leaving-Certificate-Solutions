# Question 16 (a)
# Examination Number:

def get_grade(result):
    grade = "Unsuccessful"

    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"

    return grade


# Calculate and display the mean of a list of results
results = [39, 32, 62, 88, 51, 62, 64, 81, 77]  # Initialise the list
N = len(results)  # Initialise N to the number of results
total = 0         # Initialise the running total to 0

# Loop N times
for i in range(N):
    total = total + results[i]  # Running total

# Divide by the total number of results to give the mean
arithmetic_mean = total / 9

# Display the answer
print("The mean percentage mark is", arithmetic_mean)
