"""
utlis.py
Resuable input / output helper function

"""

def get_string_input(prompt):
    """
    prompt the user until they enter a non - empty string

    Args:
    prompt (str): The message to display to the user when asking for input.

    Returns :
    str : a stripped , non empty string
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(" Input cannot be empty . please try again")
        
def get_score_input(prompt , min_val=0, max_val=100):
    """
    Prompt the user until they enter a valid score within the specified range.

    Args:
    prompt (str): The message to display to the user when asking for input.
    min_val (int): The minimum acceptable score (inclusive).
    max_val (int): The maximum acceptable score (inclusive).

    Returns:
    int: A valid score within the specified range.
    """
    while True :
        raw = input(prompt).strip()
        try:
            score = float(raw)
        except ValueError:
            print(f" '(raw)' is not a valid number ")
            continue
        if min_val <= score <=max_val:
            return score
        print(f" score must be between (min_val) and (max_val) ")
            