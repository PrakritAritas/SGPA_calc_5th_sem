# sgpa_calculator.py

# Dictionary to map marks to grade points
marks_to_grade_points = {
    (0, 39): 0,
    (40, 49): 4,
    (50, 54): 5,
    (55, 59): 6,
    (60, 69): 7,
    (70, 79): 8,
    (80, 89): 9,
    (90, 100): 10
}

# Dictionary to map subjects to credit points
subject_to_credit_points = {
    "21CS51(ATC)": 3,
    "21CSL581(AJS Lab)": 1,
    "21CS52(CN)": 4,
    "21CS53(DBMS)": 3,
    "21CS54(AIML)": 3,
    "21CSL55(DBMS Lab)": 1,
    "21RMI56": 2,
    "21CIV57": 1
}

def calculate_grade_point(marks):
    for mark_range, grade_point in marks_to_grade_points.items():
        if mark_range[0] <= marks <= mark_range[1]:
            return grade_point
    return None

def calculate_sgpa(subject_marks):
    total_credit_points = 0
    total_credit_points_times_grade_points = 0
    
    for subject, marks in subject_marks.items():
        credit_points = subject_to_credit_points.get(subject)
        grade_point = calculate_grade_point(marks)  # Calculate grade point based on marks

        if credit_points is not None and grade_point is not None:
            total_credit_points += credit_points
            total_credit_points_times_grade_points += credit_points * grade_point

    if total_credit_points > 0:
        sgpa = total_credit_points_times_grade_points / total_credit_points
        return sgpa
    else:
        return None
