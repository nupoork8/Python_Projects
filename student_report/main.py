"""
main.py
Entry point for the Student Report Generator.
Runs the program by collecting input and triggering report generation.
"""


# main.py
"""
main.py
Entry point for the Student Report Generator.
"""
 
from grades import SUBJECTS
from report import format_report, save_report
from utils  import get_string_input, get_score_input
 
 
def collect_student_info():
    """Collect and return student name and grade level."""
    print("\n" + "─" * 52)
    print("  STUDENT REPORT GENERATOR")
    print("─" * 52)
    name  = get_string_input("  Enter student name  : ")
    grade = get_string_input("  Enter grade level   : ")
    return name, grade


def collect_scores():
    """Collect one score per subject and return as a dict."""
    print("\n  Enter scores for each subject (0–100):")
    subject_scores = {}
    for subject in SUBJECTS:
        score = get_score_input(f'  {subject:<22}: ')
        subject_scores[subject] = score
    return subject_scores

def main():
    """Run the Student Report Generator end to end."""
    name, grade    = collect_student_info()
    subject_scores = collect_scores()
 
    report_text = format_report(name, grade, subject_scores)
 
    print("\n" + report_text)
 
    filepath = save_report(name, report_text)
    print(f"\n  ✓ Report saved to: {filepath}")
    print("─" * 52 + "\n")
 
 
if __name__ == '__main__':
    main()
