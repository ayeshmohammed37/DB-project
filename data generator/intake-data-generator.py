from faker import Faker
import random

# Set up faker to generate realistic data
fake = Faker()

# Create a function to generate SQL script
def generate_intake_sql_script(num_intakes):
    # Lists to help generate more realistic data
    manager_ids = list(range(1, 11))

    # Realistic intake names
    intake_names = [
        'Spring 2024 Cohort',
        'Summer 2024 Intensive',
        'Fall 2024 Professional Program'
    ]

    # SQL script header
    sql_script = [
        "-- Create Intake Table",
        "CREATE TABLE Intake (",
        "    IntakeID INT PRIMARY KEY,",
        "    IntakeName VARCHAR(100) NOT NULL,",
        "    ManagerID INT",
        ");",
        "",
        "-- Insert Realistic Intake Data",
        "INSERT INTO Intake (IntakeID, IntakeName, ManagerID)",
        "VALUES"
    ]

    # Generate intake records
    for i in range(1, num_intakes + 1):
        # Prepare SQL insert line
        sql_line = (
            f"    ({i}, '{intake_names[i-1]}', "
            f"{random.choice(manager_ids)})"
        )

        # Add comma for all lines except the last
        if i < num_intakes:
            sql_line += ","
        else:
            sql_line += ";"

        sql_script.append(sql_line)

    # Write to file
    with open('intake_insert.sql', 'w') as f:
        f.write("\n".join(sql_script))

    print(f"Generated SQL script for {num_intakes} intakes in intake_insert.sql")

# Generate 3 intakes
generate_intake_sql_script(3)
