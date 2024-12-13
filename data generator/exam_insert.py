import datetime
import random

def generate_insert_script(table_name, num_records):
    """Generates an SQL INSERT script for the Exam table.

    Args:
        table_name (str): The name of the table to insert into.
        num_records (int): The number of records to insert.

    Returns:
        str: The generated SQL INSERT script.
    """

    sql_script = f"INSERT INTO {table_name} (ExamID, StartTime, EndTime, TotalTime, Year, ex_Type) VALUES\n"
    for i in range(1, num_records + 1):
        start_time = datetime.datetime(2024, 1, 1) + datetime.timedelta(days=random.randint(0, 365))
        end_time = start_time + datetime.timedelta(hours=3)
        ex_type = "Exam" if i <= 22 else "Corrective"
        sql_script += f"({i}, '{start_time}', '{end_time}', 3, 2024, '{ex_type}'),\n"

    # Remove the trailing comma and newline
    sql_script = sql_script[:-2] + ";"

    return sql_script

if __name__ == "__main__":
    table_name = "Exam"
    num_records = 25
    sql_script = generate_insert_script(table_name, num_records)

    # Print the generated SQL script
    print(sql_script)

    # Write the script to a file
    with open("exam_insert.sql", "w") as f:
        f.write(sql_script)