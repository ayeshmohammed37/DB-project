import random

def generate_instructor_course_inserts(output_file='instructor_course_inserts.sql'):
    """
    Generate SQL insert statements for InstructorCourse table.
    
    Constraints:
    - InstructorID: 1 to 25
    - CourseID: 1 to 22
    - Ensure each instructor teaches at least 2 courses
    - Ensure each course has at least 1 instructor
    """
    # Track courses for each instructor and instructors for each course
    instructor_courses = {instructor_id: set() for instructor_id in range(1, 26)}
    course_instructors = {course_id: set() for course_id in range(1, 23)}
    
    # Open the output file to write SQL inserts
    with open(output_file, 'w') as f:
        # Ensure each instructor teaches at least 2 courses
        for instructor_id in range(1, 26):
            # Randomly determine number of courses (2-5)
            num_courses = random.randint(2, 5)
            
            while len(instructor_courses[instructor_id]) < num_courses:
                # Generate a random course ID
                course_id = random.randint(1, 22)
                
                # Ensure this course hasn't been added to this instructor
                if course_id not in instructor_courses[instructor_id]:
                    instructor_courses[instructor_id].add(course_id)
                    course_instructors[course_id].add(instructor_id)
                    
                    # Write INSERT statement
                    insert_stmt = f"INSERT INTO InstructorCourse (InstructorID, CourseID) VALUES ({instructor_id}, {course_id});\n"
                    f.write(insert_stmt)
        
        # Ensure each course has at least 1 instructor
        for course_id, instructors in course_instructors.items():
            if not instructors:
                # If no instructor, randomly assign one
                instructor_id = random.randint(1, 25)
                
                # Write INSERT statement
                insert_stmt = f"INSERT INTO InstructorCourse (InstructorID, CourseID) VALUES ({instructor_id}, {course_id});\n"
                f.write(insert_stmt)
                course_instructors[course_id].add(instructor_id)
                instructor_courses[instructor_id].add(course_id)
        
        print(f"SQL insert statements generated in {output_file}")
        
        # Print some statistics
        print("\nGeneration Statistics:")
        print("Courses per Instructor:")
        for instructor_id, courses in instructor_courses.items():
            print(f"Instructor {instructor_id}: {len(courses)} courses")
        
        print("\nInstructors per Course:")
        for course_id, instructors in course_instructors.items():
            print(f"Course {course_id}: {len(instructors)} instructors")

# Run the generation
generate_instructor_course_inserts()
