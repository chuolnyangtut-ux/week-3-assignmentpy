count = 1
total = 0

# BUG: Missing colon (:) at the end of the while statement (SyntaxError)
while count <= 5:  # BUG: Changed '<' to '<=' so that loop includes 5, fixing the wrong calculation (10 instead of 15)
    total = total + count
    count = count + 1

# BUG: Cannot concatenate str and int directly (TypeError); converted total to str(total)
print("Sum of 1 to 5 is: " + str(total))
