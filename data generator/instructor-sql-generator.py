import random

def generate_first_names():
    """Generate a list of realistic first names."""
    return [
        "Michael", "Sarah", "David", "Emily", "John", "Jennifer", 
        "Robert", "Lisa", "William", "Jessica", "James", "Amanda", 
        "Daniel", "Elizabeth", "Matthew", "Nicole", "Christopher", 
        "Lauren", "Andrew", "Samantha", "Thomas", "Rachel", 
        "Kevin", "Melissa", "Brian", "Karen", "Mark"
    ]

def generate_last_names():
    """Generate a list of realistic last names."""
    return [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", 
        "Davis", "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", 
        "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", 
        "Thompson", "White", "Lopez", "Lee", "Harris", "Clark", "Lewis"
    ]

def generate_email(first_name, last_name):
    """Generate a realistic email address."""
    email_formats = [
        f"{first_name.lower()}.{last_name.lower()}@university.edu",
        f"{first_name.lower()}{last_name.lower()}@university.edu",
        f"{first_name[0].lower()}{last_name.lower()}@university.edu"
    ]
    return random.choice(email_formats)

def generate_phone_number():
    """Generate a realistic US phone number."""
    area_codes = [
        '212', '315', '518', '607', '716', '845', '914',  # New York
        '617', '781', '857', '978',  # Massachusetts
        '415', '510', '650', '925',  # California Bay Area
        '312', '630', '708', '773',  # Illinois
        '202', '301', '240', '703'   # Washington DC area
    ]
    return f"{random.choice(area_codes)}-{random.randint(200,999)}-{random.randint(1000,9999)}"

def generate_instructor_inserts(output_file='instructor_inserts.sql'):
    """
    Generate SQL insert statements for Instructor table.
    
    Constraints:
    - InstructorID: 1 to 25
    - AccountID: 101 to 125
    - Realistic names, emails, and phone numbers
    """
    first_names = generate_first_names()
    last_names = generate_last_names()
    
    # Open the output file to write SQL inserts
    with open(output_file, 'w') as f:
        # Iterate through instructor IDs
        for instructor_id in range(1, 26):
            # Randomly select a name
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            full_name = f"{first_name} {last_name}"
            
            # Generate email and phone
            email = generate_email(first_name, last_name)
            phone = generate_phone_number()
            
            # Account ID is sequential from 101 to 125
            account_id = 100 + instructor_id
            
            # Prepare INSERT statement
            insert_stmt = (
                f"INSERT INTO Instructor (InstructorID, Name, Email, Phone, AccountID) "
                f"VALUES ({instructor_id}, '{full_name}', '{email}', '{phone}', {account_id});\n"
            )
            
            # Write to file
            f.write(insert_stmt)
        
        print(f"SQL insert statements generated in {output_file}")

# Run the generation
generate_instructor_inserts()
