from random import randrange


def generate_insert_script(table_name, num_students, num_courses):
    """Generates an SQL INSERT script for the StudentCourse table.

    Args:
        table_name (str): The name of the table to insert into.
        num_students (int): The number of students.
        num_courses (int): The number of courses.

    Returns:
        str: The generated SQL INSERT script.
    """

    sql_script = f"INSERT INTO {table_name} (ExamID, StudentID) VALUES\n"
    for student_id in range(1, num_students + 1, 1):
        course_ids = randrange(1,26)
        sql_script += f"({student_id}, {course_ids}),\n"

    # Remove the trailing comma and newline
    sql_script = sql_script[:-2] + ";"

    return sql_script

if __name__ == "__main__":
    table_name = "StudentCourse"
    num_students = 1500
    num_courses = 25
    sql_script = generate_insert_script(table_name, num_students, num_courses)

    # Print the generated SQL script
    print(sql_script)

    # Write the script to a file
    with open("StudentCourse_insert.sql", "w") as f:
        f.write(sql_script)