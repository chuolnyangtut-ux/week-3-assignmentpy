scores = [72, 45, 90, 61, 38]

# Initialize variables to keep track of counts and totals
passed_count = 0
failed_count = 0
total_score = 0

# 1. Use a for loop to go through every score in the list
for score in scores:
    total_score += score

    # 2. Work out the letter grade using if / elif / else
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    # 3. Print each score with its grade
    print(f"Score: {score} -> Grade: {grade}")

    # 4. Count passes (50 or more) and fails
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

# 5. Calculate average rounded to one decimal place
average = round(total_score / len(scores), 1)

# Summary output
print("-" * 25)
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Average score: {average}")
