# Student Grade Management System
# PSP Assignment - Part 2 (ii)
#
# Reads marks for one or more students, calculates the average mark,
# gives a letter grade (and grade point) and prints a results table.
# Run with:  python grade_manager.py

MAX_SUBJECTS = 10

# Grading scale used in our university: (minimum average, letter, grade point)
# Checked from the top, so the first row the average reaches is the grade.
GRADE_SCALE = [
    (90, "A+", 4.00),
    (85, "A", 4.00),
    (80, "A-", 3.75),
    (75, "B+", 3.50),
    (70, "B", 3.00),
    (65, "B-", 2.75),
    (60, "C+", 2.50),
    (50, "C", 2.00),
    (45, "C-", 1.75),
    (40, "D", 1.00),
    (0, "F", 0.00),
]


def read_name():
    """Ask for a student name until something is typed."""
    while True:
        name = input("Student name: ").strip()
        if name != "":
            return name
        print("  Name cannot be empty. Try again.")


def read_int(prompt, low, high):
    """Ask for a whole number between low and high (inclusive)."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if low <= value <= high:
            return value
        print(f"  Number must be between {low} and {high}.")


def read_mark(prompt):
    """Ask for a mark out of 100. Decimals like 72.5 are allowed."""
    while True:
        text = input(prompt).strip()
        try:
            mark = float(text)
        except ValueError:
            print("  Mark must be a number, e.g. 75 or 82.5")
            continue
        if 0 <= mark <= 100:
            return mark
        print("  Mark must be between 0 and 100.")


def calculate_average(marks):
    # rounded to 2 decimals so the grade matches the number that is printed
    return round(sum(marks) / len(marks), 2)


def letter_grade(average):
    """Return (letter, grade point) for an average mark."""
    for minimum, letter, point in GRADE_SCALE:
        if average >= minimum:
            return letter, point
    return "F", 0.00


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("  Please answer y or n.")


def enter_student():
    """Read one student's name and marks, and work out the result."""
    name = read_name()
    count = read_int(f"Number of subjects (1-{MAX_SUBJECTS}): ", 1, MAX_SUBJECTS)
    marks = []
    for i in range(1, count + 1):
        marks.append(read_mark(f"  Mark for subject {i}: "))
    average = calculate_average(marks)
    letter, point = letter_grade(average)
    return {"name": name, "marks": marks, "average": average,
            "grade": letter, "point": point}


def show_results(students):
    line = "-" * 56
    print()
    print("RESULTS")
    print(line)
    print(f"{'No':<4}{'Name':<20}{'Subjects':>9}{'Average':>9}{'Grade':>7}{'Point':>7}")
    print(line)
    for i, s in enumerate(students, start=1):
        print(f"{i:<4}{s['name']:<20}{len(s['marks']):>9}"
              f"{s['average']:>9.2f}{s['grade']:>7}{s['point']:>7.2f}")
    print(line)
    class_average = calculate_average([s["average"] for s in students])
    print(f"Class average: {class_average:.2f}")


def main():
    print("=== Student Grade Management System ===")
    students = []
    while True:
        print(f"\nStudent #{len(students) + 1}")
        students.append(enter_student())
        if not ask_yes_no("Add another student? (y/n): "):
            break
    show_results(students)


if __name__ == "__main__":
    main()
