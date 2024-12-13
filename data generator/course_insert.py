import random

def generate_insert_script(table_name, num_records):
    """Generates an SQL INSERT script for the Course table.

    Args:
        table_name (str): The name of the table to insert into.
        num_records (int): The number of records to insert.

    Returns:
        str: The generated SQL INSERT script.
    """

    sql_script = f"INSERT INTO {table_name} (CourseID, Name, Description, MaxDegree, MinDegree, ExamID) VALUES\n"
    for i in range(1, num_records + 1):
        name = f"Course {i}: {random.choice(['Python Programming', 'Data Structures and Algorithms', 'Web Development', 'Machine Learning', 'Database Systems', 'Software Engineering', 'Cybersecurity', 'Artificial Intelligence', 'Cloud Computing', 'Network Security', 'Mobile App Development', 'IoT', 'Big Data', 'Data Science', 'Full Stack Development'])}"
        description = f"A comprehensive course on {name.split(':')[1]}."
        sql_script += f"({i}, '{name}', '{description}', 100, 50, {i}),\n"

    # Remove the trailing comma and newline
    sql_script = sql_script[:-2] + ";"

    return sql_script

if __name__ == "__main__":
    table_name = "Course"
    num_records = 22
    sql_script = generate_insert_script(table_name, num_records)

    # Print the generated SQL script
    print(sql_script)

    # Write the script to a file
    with open("course_insert.sql", "w") as f:
        f.write(sql_script)