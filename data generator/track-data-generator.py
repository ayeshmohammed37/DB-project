from faker import Faker
import random

# Set up faker to generate realistic data
fake = Faker()

# Create a function to generate SQL script
def generate_track_sql_script(num_tracks):
    # Lists to help generate more realistic data
    manager_ids = list(range(1, 11))
    department_ids = list(range(1, 5))

    # Predefined track names that sound professional and realistic
    track_names = [
        'Software Engineering Fundamentals',
        'Web Development Intensive',
        'Cloud Computing Specialization',
        'Data Science and Analytics',
        'Cybersecurity Essentials',
        'Mobile Application Development',
        'AI and Machine Learning',
        'Enterprise Software Architecture',
        'DevOps and Cloud Infrastructure',
        'Full Stack Web Technologies',
        'Business Intelligence and Reporting',
        'Network and Systems Administration',
        'Blockchain and Distributed Systems',
        'Digital Product Design',
        'Advanced Database Management'
    ]

    # SQL script header
    sql_script = [
        "-- Create Track Table",
        "CREATE TABLE Track (",
        "    TrackID INT PRIMARY KEY,",
        "    Name VARCHAR(100) NOT NULL,",
        "    ManagerID INT,",
        "    DepartmentID INT",
        ");",
        "",
        "-- Insert Realistic Track Data",
        "INSERT INTO Track (TrackID, Name, ManagerID, DepartmentID)",
        "VALUES"
    ]

    # Generate track records
    for i in range(1, num_tracks + 1):
        # Prepare SQL insert line
        sql_line = (
            f"    ({i}, '{track_names[i-1]}', "
            f"{random.choice(manager_ids)}, "
            f"{random.choice(department_ids)})"
        )

        # Add comma for all lines except the last
        if i < num_tracks:
            sql_line += ","
        else:
            sql_line += ";"

        sql_script.append(sql_line)

    # Write to file
    with open('track_insert.sql', 'w') as f:
        f.write("\n".join(sql_script))

    print(f"Generated SQL script for {num_tracks} tracks in track_insert.sql")

# Generate 15 tracks
generate_track_sql_script(15)
