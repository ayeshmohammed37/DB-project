from faker import Faker
import random

# Set up faker to generate realistic data
fake = Faker()

# Create a function to generate SQL script
def generate_branch_sql_script(num_branches):
    # Lists to help generate more realistic data
    manager_ids = list(range(1, 11))

    # Realistic branch names
    branch_names = [
        'Global Learning Center',
        'Innovation Hub Campus',
        'Professional Development Institute',
        'Metropolitan Training Campus'
    ]

    # SQL script header
    sql_script = [
        "-- Create Branch Table",
        "CREATE TABLE Branch (",
        "    BranchID INT PRIMARY KEY,",
        "    Name VARCHAR(100) NOT NULL,",
        "    ManagerID INT",
        ");",
        "",
        "-- Insert Realistic Branch Data",
        "INSERT INTO Branch (BranchID, Name, ManagerID)",
        "VALUES"
    ]

    # Generate branch records
    for i in range(1, num_branches + 1):
        # Prepare SQL insert line
        sql_line = (
            f"    ({i}, '{branch_names[i-1]}', "
            f"{random.choice(manager_ids)})"
        )

        # Add comma for all lines except the last
        if i < num_branches:
            sql_line += ","
        else:
            sql_line += ";"

        sql_script.append(sql_line)

    # Write to file
    with open('branch_insert.sql', 'w') as f:
        f.write("\n".join(sql_script))

    print(f"Generated SQL script for {num_branches} branches in branch_insert.sql")

# Generate 4 branches
generate_branch_sql_script(4)
