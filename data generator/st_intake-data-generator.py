import random

def generate_insert_script(table_name, num_records):
    """Generates an SQL INSERT script for the specified table and number of records.

    Args:
        table_name (str): The name of the table to insert into.
        num_records (int): The number of records to insert.

    Returns:
        str: The generated SQL INSERT script.
    """

    sql_script = f"INSERT INTO {table_name} (Student_ID, Intake_ID) VALUES\n"
    for i in range(1, num_records + 1):
        intake_id = random.randint(1, 3)
        sql_script += f"({i}, {intake_id}),\n"

    # Remove the trailing comma and newline
    sql_script = sql_script[:-2] + ";"

    return sql_script

if __name__ == "__main__":
    table_name = "ST_Intake"
    num_records = 1500
    sql_script = generate_insert_script(table_name, num_records)

    # Print the generated SQL script
    print(sql_script)

    # Optionally, write the script to a file
    with open("insert_script.sql", "w") as f:
        f.write(sql_script)