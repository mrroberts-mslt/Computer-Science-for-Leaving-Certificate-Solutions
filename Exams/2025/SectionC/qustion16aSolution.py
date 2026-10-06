# Question 16 (a)
# Examination Number:

def get_grade(result):
    grade = "Unsuccessful"
    
    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"
    # part iii - start
    elif result >= 50:
        grade = "Lower Merit"
    elif result >= 40:
        grade = "Pass"
    # part iii - end
    
    return grade

# Calculate and display the mean of a list of results
results = [39, 32, 62, 88, 51, 62, 64, 81, 77] # Initialise the list
N = len(results) #initialise N to the number of results
total = 0 #initialise the running total to 0

# Loop N times
for i in range(N):
    total = total + results[i] # running total

# Divide by the total number of results to give the mean
arithmetic_mean = total/N # part ii
arithmetic_mean = round(arithmetic_mean, 2) # part i
# Display the answer
print("The mean percentage mark is", arithmetic_mean)

# part (iv) - start
grade = get_grade(arithmetic_mean)
print("The grade for the average result is", grade)
# part (iv) - end

# part (v) - start
highest = max(results)
lowest = min(results)
print("The lowest score is", lowest)
print("The highest score is", highest)
# part (v) - end

# part (vi) - start
a = 0 # count of results less than 40
b = 0 # count of results between 50 and 79 inclusive
for result in results:
    if result < 40:
        a += 1
    elif result >= 50 and result <= 79:
        b += 1
print("The number of scores below 40 is", a)
print("The number of scores between 50 and 79 inclusive is", b)
# part (vi) - end

# part (vii) - start
longest_run = []
current_run = [results[0]]

for i in range(1, N):
    if results[i] > results[i - 1]:
        current_run.append(results[i])
    else:
        if len(current_run) > len(longest_run):
            longest_run = current_run
        current_run = [results[i]]

# Check one last time at the end of the loop
if len(current_run) > len(longest_run):
    longest_run = current_run

print("Longest run of result increases is", longest_run)
# part (vii) - end
