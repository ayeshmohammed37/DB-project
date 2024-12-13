import random
import sqlite3

def generate_st_exam_inserts(output_file='st_exam_inserts.sql'):
    """
    Generate SQL insert statements for St_Exam table.
    
    Constraints:
    - ExamID: 1 to 25
    - StudentID: 1 to 1500
    - Each exam has 60 to 120 unique students
    """
    # Prepare to track which students have taken which exams to ensure uniqueness
    exam_students = {}
    
    # Open the output file to write SQL inserts
    with open(output_file, 'w') as f:
        # Iterate through each exam (1-25)
        for exam_id in range(1, 26):
            # Randomly determine number of students for this exam (60-120)
            num_students = random.randint(60, 120)
            
            # Track students for this exam
            exam_students[exam_id] = set()
            
            # Generate unique student entries for this exam
            while len(exam_students[exam_id]) < num_students:
                # Generate a random student ID
                student_id = random.randint(1, 1500)
                
                # Ensure this student hasn't already been added to this exam
                if student_id not in exam_students[exam_id]:
                    exam_students[exam_id].add(student_id)
                    
                    # Write INSERT statement
                    insert_stmt = f"INSERT INTO St_Exam (ExamID, StudentID) VALUES ({exam_id}, {student_id});\n"
                    f.write(insert_stmt)
        
        print(f"SQL insert statements generated in {output_file}")
        
        # Print some statistics
        print("\nGeneration Statistics:")
        for exam_id, students in exam_students.items():
            print(f"Exam {exam_id}: {len(students)} students")

# Run the generation
generate_st_exam_inserts()
