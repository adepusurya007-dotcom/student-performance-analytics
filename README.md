# Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System** – Python with AI (EWB Courses) project assignment

- **Student:** Surya
- **PIN:** 23086-EI-052
- **Course / Institute:** Diploma in Electronics and Instrumentation Engineering (EIE), Government Polytechnic, Bellampalli

## 2. Objective
Teachers often have to calculate totals, averages, grades and pass/fail status for every student by hand, which is slow and error-prone. This project automates that work: it reads student records from a CSV file, processes them with NumPy and Pandas, and prints a clear performance report (grades, pass/fail statistics, subject-wise analysis and top performers).

## 3. Technologies Used
- Python 3
- NumPy – numerical calculations (sum, mean, min, max)
- Pandas – loading the CSV, DataFrame operations, sorting, grouping

## 4. Dataset Description
`students.csv` contains **20 student records** with 9 columns:

| Column | Meaning |
|---|---|
| Student_ID, Name, Department | Student details (EIE, ECE, CSE, EEE) |
| Maths, Physics, Programming, Electronics, English | Subject marks out of 100 |
| Attendance | Attendance percentage |

## 5. Implementation
1. **Load data** – `load_data()` reads `students.csv` into a Pandas DataFrame; shape, columns and first records are displayed.
2. **Total & average** – `add_total_and_average()` converts the marks to a NumPy array and uses `np.sum` / `np.mean` row-wise.
3. **Pass/Fail rule** – a student passes only if they score **at least 40 in every subject** (`get_result()`).
4. **Grading rule** – based on average: A+ ≥ 90, A ≥ 80, B ≥ 70, C ≥ 60, D ≥ 50, E ≥ 40, otherwise F. A student who fails any subject gets F (`get_grade()`).
5. **Loops** – `add_result_and_grade()` loops over each student to assign result, grade and attendance status (shortage if attendance < 75%); `subject_analysis()` loops over each subject.
6. **Analysis** – class statistics, highest/lowest average, subject-wise analysis, top 5 performers, grade distribution, department-wise average and the list of failed students.
7. **Save results** – processed data is written to `results.csv`.

## 6. Key Features
- `load_data()` – reads the dataset
- `add_total_and_average()` – total and average marks using NumPy
- `get_result()` / `get_grade()` – clearly defined pass/fail and grading rules
- `add_result_and_grade()` – result, grade and attendance status for all students
- `subject_analysis()` – average, highest, lowest, pass count and topper per subject
- `top_performers()` – ranks the best students
- `class_statistics()` – pass percentage, class average and more

## 7. Output
Run `python main.py`. Full output is saved in `output.txt`. Sample:

```
Total students        : 20
Passed                : 18
Failed                : 2
Pass percentage       : 90.0
Class average         : 70.59

Best performing subject: Programming

 Rank Student_ID         Name Department  Total  Average Grade
    1       S008   Divya Teja        CSE    467     93.4    A+
    2       S002 Anjali Reddy        EIE    448     89.6     A
    3       S014   Swathi Rao        EIE    439     87.8     A
    4       S004 Sneha Sharma        CSE    438     87.6     A
    5       S016  Harika Devi        CSE    411     82.2     A
```

## 8. Final Outcome
The project reads the dataset and produces a complete, easy-to-read analysis: 18 of 20 students passed (90%), the class average is 70.59, Divya Teja is the top performer (93.4 average), Programming is the best subject, and 4 students have an attendance shortage.

## 9. Challenges & Learning
- **Pass/fail vs grade mismatch:** a student could have a decent average but fail one subject. I solved this by making the pass rule per-subject and giving grade F to anyone who fails a subject.
- **Mixing NumPy and Pandas:** learned to convert DataFrame columns with `.to_numpy()` for fast calculations and use `axis=1` for row-wise operations.
- **Code organisation:** moving reusable logic into `functions.py` kept `main.py` short and readable.

## 10. GitHub Repository
https://github.com/<your-username>/student-performance-analytics

## How to Run
```bash
pip install numpy pandas
python main.py
```

## Project Structure
```
student-performance-analytics/
├── main.py          # runs the analysis and prints the report
├── functions.py     # reusable functions
├── students.csv     # dataset (20 records)
├── results.csv      # generated processed results
├── output.txt       # sample program output
└── README.md        # project documentation
```
