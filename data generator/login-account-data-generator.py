import random
import string

def generate_random_password(length=12):
    """Generate a random password without single quotes or double dashes"""
    # Remove problematic characters
    safe_chars = string.ascii_letters + string.digits + '!@#$%^&*()_+=[]{};:,.<>?'
    
    while True:
        password = ''.join(random.choice(safe_chars) for _ in range(length))
        
        # Ensure no single quotes or double dashes
        if "'" not in password and '--' not in password:
            return password

def generate_login_account_sql_script():
    # SQL script header
    sql_script = [
        "-- Create LoginAccount Table",
        "CREATE TABLE LoginAccount (",
        "    AccountID INT PRIMARY KEY,",
        "    Username VARCHAR(50) NOT NULL,",
        "    Password VARCHAR(100) NOT NULL,",
        "    Role VARCHAR(20) NOT NULL",
        ");",
        "",
        "-- Insert Realistic Login Account Data",
        "INSERT INTO LoginAccount (AccountID, Username, Password, Role)",
        "VALUES"
    ]

    # Will store all generated records
    login_records = []

    # Managers (1 to 10)
    for i in range(1, 11):
        record = (
            f"    ({i}, 'Manager{i}', "
            f"'{generate_random_password()}', 'Manager')"
        )
        login_records.append(record)

    # Instructors (101 to 125)
    for i in range(101, 126):
        record = (
            f"    ({i}, 'Instructor{i}', "
            f"'{generate_random_password()}', 'Instructor')"
        )
        login_records.append(record)

    # Students (1000 to 1500)
    for i in range(1000, 2501):
        record = (
            f"    ({i}, 'Student{i}', "
            f"'{generate_random_password()}', 'Student')"
        )
        login_records.append(record)

    # Add comma to all lines except the last
    for i in range(len(login_records) - 1):
        login_records[i] += ","

    # Add semicolon to the last line
    login_records[-1] += ";"

    # Combine all parts of the SQL script
    sql_script.extend(login_records)

    # Write to file
    with open('login_account_insert.sql', 'w') as f:
        f.write("\n".join(sql_script))

    print(f"Generated SQL script for LoginAccount in login_account_insert.sql")
    print(f"Total records: {len(login_records)}")

# Generate LoginAccount data
generate_login_account_sql_script()