"""
report.py

formats student data into a readable report and savs it to disk
"""

import os
from datetime import datetime
from grades import calculate_average , assign_letter_grade , assign_performance

OUTPUT_DIR = 'outputs'

def format_report(student_name, grade_level, subject_scores):
    """
    Build a formatted report string from student data.
 
    Args:
        student_name   (str):         Full name of the student.
        grade_level    (str):         e.g. 'Grade 10'.
        subject_scores (dict):        {subject: score} mapping.
 
    Returns:
        str: A multi-line formatted report.
    """
    now       = datetime.now().strftime('%d %B %Y, %H:%M')
    scores    = list(subject_scores.values())
    average   = calculate_average(scores)
    letter    = assign_letter_grade(average)
    perf      = assign_performance(average)
 
    width = 52
    sep   = '=' * width
    line  = '-' * width
 
    lines = [
        sep,
        '  STUDENT ACADEMIC REPORT'.center(width),
        sep,
        f'  Name        : {student_name}',
        f'  Grade Level : {grade_level}',
        f'  Generated   : {now}',
        line,
        '  SUBJECT SCORES',
        line,
    ]
 
    for subject, score in subject_scores.items():
        lines.append(f'  {subject:<22} {score:>6.1f}')
 
    lines += [
        line,
        f'  Average Score  : {average:.2f}',
        f'  Letter Grade   : {letter}',
        f'  Performance    : {perf}',
        sep,
    ]
 
    return '\n'.join(lines)

def save_report(student_name, report_text):
    """
    Save a formatted report string to a .txt file.
 
    Args:
        student_name (str): Used to name the output file.
        report_text  (str): The formatted report string.
 
    Returns:
        str: The full path to the saved file.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
 
    safe_name = student_name.replace(' ', '_').lower()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename  = f'{safe_name}_{timestamp}.txt'
    filepath  = os.path.join(OUTPUT_DIR, filename)
 
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(report_text)
 
    return filepath
