import random

def generate_instructor_exam_inserts(output_file='instructor_exam_inserts.sql'):
    """
    Generate SQL insert statements for InstructorExam table.
    
    Constraints:
    - InstructorID: 1 to 25
    - ExamID: 1 to 25
    - Ensure each instructor is responsible for multiple exams
    - Ensure each exam has at least one responsible instructor
    """
    # Track exams for each instructor and instructors for each exam
    instructor_exams = {instructor_id: set() for instructor_id in range(1, 26)}
    exam_instructors = {exam_id: set() for exam_id in range(1, 26)}
    
    # Open the output file to write SQL inserts
    with open(output_file, 'w') as f:
        # Ensure each instructor is responsible for multiple exams
        for instructor_id in range(1, 26):
            # Randomly determine number of exams (2-5)
            num_exams = random.randint(2, 5)
            
            while len(instructor_exams[instructor_id]) < num_exams:
                # Generate a random exam ID
                exam_id = random.randint(1, 25)
                
                # Ensure this exam hasn't been added to this instructor
                if exam_id not in instructor_exams[instructor_id]:
                    instructor_exams[instructor_id].add(exam_id)
                    exam_instructors[exam_id].add(instructor_id)
                    
                    # Write INSERT statement
                    insert_stmt = f"INSERT INTO InstructorExam (InstructorID, ExamID) VALUES ({instructor_id}, {exam_id});\n"
                    f.write(insert_stmt)
        
        # Ensure each exam has at least 1 instructor
        for exam_id, instructors in exam_instructors.items():
            if not instructors:
                # If no instructor, randomly assign one
                instructor_id = random.randint(1, 25)
                
                # Write INSERT statement
                insert_stmt = f"INSERT INTO InstructorExam (InstructorID, ExamID) VALUES ({instructor_id}, {exam_id});\n"
                f.write(insert_stmt)
                exam_instructors[exam_id].add(instructor_id)
                instructor_exams[instructor_id].add(exam_id)
        
        print(f"SQL insert statements generated in {output_file}")
        
        # Print some statistics
        print("\nGeneration Statistics:")
        print("Exams per Instructor:")
        for instructor_id, exams in instructor_exams.items():
            print(f"Instructor {instructor_id}: {len(exams)} exams")
        
        print("\nInstructors per Exam:")
        for exam_id, instructors in exam_instructors.items():
            print(f"Exam {exam_id}: {len(instructors)} instructors")

# Run the generation
generate_instructor_exam_inserts()
