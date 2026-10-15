"""Student Performance Analytics System - main program."""

import pandas as pd
from functions import (SUBJECTS, load_data, add_total_and_average,
                       add_result_and_grade, subject_analysis,
                       top_performers, class_statistics)

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def heading(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    # Step 2 - Read the data
    df = load_data("students.csv")
    heading("1. DATASET OVERVIEW")
    print(f"Records: {df.shape[0]} | Columns: {df.shape[1]}")
    print("Columns:", list(df.columns))
    print("\nFirst 5 records:")
    print(df.head())

    # Step 3 - Process the data
    df = add_total_and_average(df)
    df = add_result_and_grade(df)

    heading("2. STUDENT RESULTS (Total, Average, Grade, Result)")
    print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Result",
              "Attendance_Status"]].to_string(index=False))

    # Step 4 - Analysis
    heading("3. CLASS STATISTICS")
    for key, value in class_statistics(df).items():
        print(f"{key:<22}: {value}")

    best = df.loc[df["Average"].idxmax()]
    worst = df.loc[df["Average"].idxmin()]
    print(f"\nHighest average: {best['Name']} ({best['Average']})")
    print(f"Lowest average : {worst['Name']} ({worst['Average']})")

    heading("4. SUBJECT-WISE PERFORMANCE")
    subj = subject_analysis(df)
    print(subj.to_string(index=False))
    best_subject = subj.loc[subj["Average"].idxmax(), "Subject"]
    print(f"\nBest performing subject: {best_subject}")

    heading("5. TOP 5 PERFORMERS")
    print(top_performers(df, 5).to_string(index=False))

    heading("6. GRADE DISTRIBUTION")
    print(df["Grade"].value_counts().sort_index().to_string())

    heading("7. DEPARTMENT-WISE AVERAGE")
    print(df.groupby("Department")["Average"].mean().round(2).to_string())

    heading("8. FAILED STUDENTS")
    failed = df[df["Result"] == "Fail"]
    for _, row in failed.iterrows():          # loop over failed students
        weak = [s for s in SUBJECTS if row[s] < 40]
        print(f"{row['Name']} - failed in: {', '.join(weak)}")

    # Save processed results
    df.to_csv("results.csv", index=False)
    print("\nProcessed results saved to results.csv")


if __name__ == "__main__":
    main()
