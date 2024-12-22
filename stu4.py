from fpdf import FPDF

def main_menu():
    print("\n=== Student Grade Tracker ===")
    print("1. Add Student Grades")
    print("2. Generate PDF Grade Cards")
    print("3. Exit")
    return input("Choose an option (1-3): ")

def calculate_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gpa(average):
    if average >= 100:
        return 10.0
    elif average >= 90:
        return 9.0
    elif average >= 80:
        return 8.0
    elif average >= 70:
        return 7.0
    elif average >= 60:
        return 6.0
    else:
        return 0.0

def add_student_grades(students):
    name = input("Enter student name: ")
    subjects = {}
    while True:
        subject = input("Enter subject name (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        
        print(f"\nEntering grades for {subject}")
        assignments = []
        while True:
            try:
                grade = input(f"Enter grade for an assignment in {subject} (or type 'done' to finish): ")
                if grade.lower() == 'done':
                    break
                assignments.append(float(grade))
            except ValueError:
                print("Invalid grade. Please enter a number.")
        
        try:
            theory_grade = float(input(f"Enter grade for theory paper in {subject}: "))
        except ValueError:
            print("Invalid grade. Please enter a number.")
            continue
        
        subjects[subject] = {"Assignments": assignments, "Theory Paper": theory_grade}
    
    students[name] = subjects
    print(f"Grades added for {name}.")

def generate_pdf_grade_cards(students):
    if not students:
        print("No student records found.")
        return

    for name, subjects in students.items():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(200, 10, txt=f"Grade Card for {name}", ln=True, align='C')
        pdf.ln(10)
        
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 10, txt="Subject Grades:", ln=True, align='L')
        
        total_avg = 0
        subject_count = 0
        
        pdf.set_font("Arial", size=10)
        pdf.cell(60, 10, txt="Subject", border=1, align='C')
        pdf.cell(40, 10, txt="Assignments Avg", border=1, align='C')
        pdf.cell(40, 10, txt="Theory Grade", border=1, align='C')
        pdf.cell(40, 10, txt="Overall Avg", border=1, align='C')
        pdf.cell(10, 10, txt="Grade", border=1, align='C')
        pdf.ln(10)
        
        for subject, grades in subjects.items():
            assignments = grades["Assignments"]
            theory_grade = grades["Theory Paper"]
            avg_assignments = sum(assignments) / len(assignments) if assignments else 0
            overall_avg = (avg_assignments + theory_grade) / 2
            letter_grade = calculate_letter_grade(overall_avg)
            
            pdf.cell(60, 10, txt=subject, border=1)
            pdf.cell(40, 10, txt=f"{avg_assignments:.2f}", border=1, align='C')
            pdf.cell(40, 10, txt=f"{theory_grade:.2f}", border=1, align='C')
            pdf.cell(40, 10, txt=f"{overall_avg:.2f}", border=1, align='C')
            pdf.cell(10, 10, txt=letter_grade, border=1, align='C')
            pdf.ln(10)
            
            total_avg += overall_avg
            subject_count += 1
        
        overall_average = total_avg / subject_count if subject_count else 0
        overall_letter_grade = calculate_letter_grade(overall_average)
        overall_gpa = calculate_gpa(overall_average)
        
        pdf.ln(5)
        pdf.set_font("Arial", size=12, style='B')
        pdf.cell(0, 10, txt=f"Overall Average: {overall_average:.2f}", ln=True, align='L')
        pdf.cell(0, 10, txt=f"Overall Letter Grade: {overall_letter_grade}", ln=True, align='L')
        pdf.cell(0, 10, txt=f"Overall GPA: {overall_gpa:.2f}", ln=True, align='L')
        
        file_name = f"{name}_grade_card.pdf"
        pdf.output(file_name)
        print(f"Grade card generated: {file_name}")

def main():
    students = {}
    while True:
        choice = main_menu()
        if choice == '1':
            add_student_grades(students)
        elif choice == '2':
            generate_pdf_grade_cards(students)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()