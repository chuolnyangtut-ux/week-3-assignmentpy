
# Week 3 Assignment: Grade Reporter & Bug Hunt

This repository contains Python solutions for the Week 3 assignment on conditions and loops.

## Files Included
- `grade_reporter.py`: Calculates letter grades for a list of scores, counts the number of passes and fails, and calculates the rounded average score.
- `bug_hunt.py`: A fixed program that sums numbers from 1 to 5 with comments explaining the three bugs found.

## Bug Hunt Reflection
The logic bug where the loop condition was `count < 5` was the hardest to find because Python executed the program without throwing any error message. I knew something was wrong because the sum returned `10` instead of the expected `15`, indicating that the number 5 was omitted during iteration.
