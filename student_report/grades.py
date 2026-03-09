"""
grades.py
Contains all grading logic: score validation, average calculation,
letter grade assignment, and performance classification.
"""

# Grade Boundaries
GRADE_A = 90  # score >= 90 earn an A
GRADE_B = 80  # score >= 80 and < 90 earn a B
GRADE_C = 70  # score >= 70 and < 80 earn a C
GRADE_D = 60  # score >= 60 and < 70 earn a D
# score < 60 earn an F

# Score constraints
MIN_SCORE = 0
MAX_SCORE = 100

# Performance Labels
PERFORMANCE_EXCELLENT = 'Excellent'
PERFORMANCE_GOOD = 'Good'
PERFORMANCE_AVERAGE = 'Average'
PERFORMANCE_POOR = 'Poor'

# Subjects
SUBJECTS = [
    'Mathematics',
    'Science',
    'English',
    'History',
    'Physical Education'
]


def calculate_average(scores):
    """Calculate average score of a list of scores."""
    if not scores:
        raise ValueError("Cannot calculate average of an empty list")

    return round(sum(scores) / len(scores), 2)


def assign_letter_grade(average):
    """Return letter grade based on average."""
    if average >= GRADE_A:
        return 'A'
    elif average >= GRADE_B:
        return 'B'
    elif average >= GRADE_C:
        return 'C'
    elif average >= GRADE_D:
        return 'D'
    else:
        return 'F'


def assign_performance(average):
    """Return performance label based on average."""
    if average >= GRADE_A:
        return PERFORMANCE_EXCELLENT
    elif average >= GRADE_B:
        return PERFORMANCE_GOOD
    elif average >= GRADE_C:
        return PERFORMANCE_AVERAGE
    else:
        return PERFORMANCE_POOR