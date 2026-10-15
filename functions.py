"""Reusable functions for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

# ---- Project settings (grading rule + pass condition) ----
SUBJECTS = ["Maths", "Physics", "Programming", "Electronics", "English"]
PASS_MARK = 40          # a student must score at least this in EVERY subject
MIN_ATTENDANCE = 75     # attendance (%) required to avoid a shortage warning

# Grading rule based on average marks (any failed subject => grade F)
GRADE_RULE = [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D"), (40, "E")]


def load_data(path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(path)


def add_total_and_average(df, subjects=SUBJECTS):
    """Add Total and Average columns using NumPy."""
    marks = df[subjects].to_numpy()               # DataFrame -> NumPy array
    df["Total"] = np.sum(marks, axis=1)           # row-wise total
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def get_result(subject_marks):
    """Pass only if the student scored >= PASS_MARK in every subject."""
    return "Pass" if np.min(subject_marks) >= PASS_MARK else "Fail"


def get_grade(average, result):
    """Return a grade from the average; failed students always get F."""
    if result == "Fail":
        return "F"
    for cutoff, grade in GRADE_RULE:
        if average >= cutoff:
            return grade
    return "F"


def add_result_and_grade(df, subjects=SUBJECTS):
    """Loop over every student and add Result, Grade and Attendance_Status."""
    results, grades, att_status = [], [], []
    for _, row in df.iterrows():
        result = get_result(row[subjects].to_numpy(dtype=float))
        results.append(result)
        grades.append(get_grade(row["Average"], result))
        att_status.append("OK" if row["Attendance"] >= MIN_ATTENDANCE else "Shortage")
    df["Result"] = results
    df["Grade"] = grades
    df["Attendance_Status"] = att_status
    return df


def subject_analysis(df, subjects=SUBJECTS):
    """Subject-wise average, highest, lowest, pass count and topper."""
    rows = []
    for subject in subjects:
        scores = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(scores)), 2),
            "Highest": int(np.max(scores)),
            "Lowest": int(np.min(scores)),
            "Passed": int(np.sum(scores >= PASS_MARK)),
            "Topper": df.loc[df[subject].idxmax(), "Name"],
        })
    return pd.DataFrame(rows)


def top_performers(df, n=5):
    """Return the top n students ranked by average marks."""
    top = df.sort_values("Average", ascending=False).head(n).copy()
    top.insert(0, "Rank", range(1, len(top) + 1))
    return top[["Rank", "Student_ID", "Name", "Department", "Total", "Average", "Grade"]]


def class_statistics(df):
    """Overall class statistics as a dictionary."""
    avg = df["Average"].to_numpy()
    return {
        "Total students": len(df),
        "Passed": int((df["Result"] == "Pass").sum()),
        "Failed": int((df["Result"] == "Fail").sum()),
        "Pass percentage": round(float((df["Result"] == "Pass").mean() * 100), 2),
        "Class average": round(float(np.mean(avg)), 2),
        "Highest average": float(np.max(avg)),
        "Lowest average": float(np.min(avg)),
        "Attendance shortage": int((df["Attendance_Status"] == "Shortage").sum()),
    }
