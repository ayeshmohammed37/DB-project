from faker import Faker
import random

# Set up faker to generate realistic data
fake = Faker()

# Create a function to generate SQL script
def generate_student_sql_script(num_students):
    # Lists to help generate more realistic data
    intake_ids = [1, 2, 3]
    manager_ids = list(range(1, 11))
    branch_ids = list(range(1, 5))
    track_ids = list(range(1, 16))

    # SQL script header
    sql_script = [
        "-- Create Student Table",
        "CREATE TABLE IF NOT EXISTS Student (",
        "    StudentID INT PRIMARY KEY,",
        "    Name VARCHAR(100) NOT NULL,",
        "    Email VARCHAR(100),",
        "    Phone VARCHAR(15),",
        "    IntakeID INT,",
        "    AccountID INT,",
        "    ManagerID INT,",
        "    BranchID INT,",
        "    TrackID INT",
        ");",
        "",
        "-- Insert Realistic Student Data",
        "INSERT INTO Student (StudentID, Name, Email, Phone, IntakeID, AccountID, ManagerID, BranchID, TrackID)",
        "VALUES"
    ]

    # Track used emails and account IDs to ensure uniqueness
    used_emails = set()
    used_account_ids = set()

    # Generate student records
    for i in range(1, num_students + 1):
        # Ensure unique email
        while True:
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = f"{first_name.lower()}.{last_name.lower()}@example.com"
            if email not in used_emails:
                used_emails.add(email)
                break

        # Ensure unique account ID between 1000 and 2500
        while True:
            account_id = random.randint(1000, 2500)
            if account_id not in used_account_ids:
                used_account_ids.add(account_id)
                break

        # Prepare SQL insert line
        sql_line = (
            f"    ({i}, '{first_name} {last_name}', '{email}', "
            f"'555-{random.randint(100,999)}-{random.randint(1000,9999)}', "
            f"{random.choice(intake_ids)}, {account_id}, "
            f"{random.choice(manager_ids)}, {random.choice(branch_ids)}, "
            f"{random.choice(track_ids)})"
        )

        # Add comma for all lines except the last
        if i < num_students:
            sql_line += ","
        else:
            sql_line += ";"

        sql_script.append(sql_line)

    # Write to file
    with open('student_insert.sql', 'w') as f:
        f.write("\n".join(sql_script))

    print(f"Generated SQL script for {num_students} students in student_insert.sql")

# Generate 1500 students
generate_student_sql_script(1500)