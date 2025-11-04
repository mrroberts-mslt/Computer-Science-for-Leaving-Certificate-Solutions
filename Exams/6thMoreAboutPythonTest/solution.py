# --- SOLUTION CODE ---

names = ["Ava", "Ben", "Ciara", "Dara", "Eoin", "Fiona"]
scores = [88, 54, 72, 39, 100, 67]

def grade_band(score):
    """Return a letter grade based on the score using conditionals."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"

def passed(score):
    """Return True if the student passed (score >= 40)."""
    if score >= 40:
        return True
    else:
        return False

# --- DRIVER CODE ---
print("Name    Score  Grade  Pass?")
print("-" * 30)

# initialise summary variables
count = 0
total = 0
highest = scores[0]
lowest = scores[0]
passed_count = 0

# loop through all students
for i in range(len(names)):
    name = names[i]
    score = scores[i]

    band = grade_band(score)
    pass_flag = passed(score)

    # print row of results
    print(f"{name:<7} {score:<6} {band:<6} {pass_flag}")

    # update counters
    count += 1
    total += score
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
    if pass_flag:
        passed_count += 1

# calculate average
average = total / count

# summary section
print("\nSummary")
print("-------")
print("Students:", count)
print("Average: ", round(average, 1))
print("Highest: ", highest)
print("Lowest:  ", lowest)
print("Passed:  ", passed_count)
