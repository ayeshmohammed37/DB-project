import random
import sqlite3

def generate_multiple_choice_question(question_id):
    """Generate a multiple-choice question."""
    subjects = [
        "Mathematics", "Science", "History", "Literature", 
        "Computer Science", "Physics", "Chemistry", "Biology"
    ]
    
    subject = random.choice(subjects)
    
    questions = [
        f"Which of the following is a key concept in {subject}?",
        f"What is the primary characteristic of a fundamental principle in {subject}?",
        f"Select the most accurate statement about {subject}:",
        f"Identify the correct approach to understanding {subject}:"
    ]
    
    question_text = f"QuestionText({question_id}): {random.choice(questions)}"
    
    # Generate multiple choice options
    options = [
        f"Option A: Theoretical approach in {subject}",
        f"Option B: Practical application of {subject}",
        f"Option C: Advanced methodology in {subject}",
        f"Option D: Fundamental principle of {subject}"
    ]
    
    correct_answer = f"CorrectAnswer({question_id}): {random.choice(options)}"
    best_answer = f"BestAnswer({question_id}): Comprehensive explanation of {subject} principles"
    multiple_choice = "TRUE"
    true_false = "FALSE"
    text = "FALSE"
    
    return question_text, correct_answer, best_answer, multiple_choice, true_false, text

def generate_true_false_question(question_id):
    """Generate a true/false question."""
    subjects = [
        "Scientific Method", "Historical Events", "Mathematical Theorems", 
        "Literary Analysis", "Computer Programming", "Biological Processes"
    ]
    
    subject = random.choice(subjects)
    
    questions = [
        f"In {subject}, is this statement true or false?",
        f"Determine the validity of this principle in {subject}:",
        f"Evaluate the accuracy of this concept in {subject}:"
    ]
    
    question_text = f"QuestionText({question_id}): {random.choice(questions)} Statement: {subject} has significant impact on modern understanding."
    
    # Randomly choose true or false
    is_true = random.choice([True, False])
    correct_answer = f"CorrectAnswer({question_id}): {'TRUE' if is_true else 'FALSE'}"
    best_answer = f"BestAnswer({question_id}): Detailed explanation of {subject} principles"
    multiple_choice = "FALSE"
    true_false = "TRUE"
    text = "FALSE"
    
    return question_text, correct_answer, best_answer, multiple_choice, true_false, text

def generate_text_question(question_id):
    """Generate a text-based question."""
    subjects = [
        "Scientific Research", "Historical Analysis", "Mathematical Problem Solving", 
        "Literary Interpretation", "Computer Systems", "Biological Investigation"
    ]
    
    subject = random.choice(subjects)
    
    questions = [
        f"Provide a comprehensive analysis of a key concept in {subject}.",
        f"Explain the significance and implications of a principle in {subject}.",
        f"Discuss the evolution and impact of a methodology in {subject}:"
    ]
    
    question_text = f"QuestionText({question_id}): {random.choice(questions)}"
    correct_answer = f"CorrectAnswer({question_id}): Detailed exploration of {subject} principles"
    best_answer = f"BestAnswer({question_id}): Comprehensive and nuanced explanation of {subject}"
    multiple_choice = "FALSE"
    true_false = "FALSE"
    text = "TRUE"
    
    return question_text, correct_answer, best_answer, multiple_choice, true_false, text

def generate_question_inserts(output_file='question_inserts.sql'):
    """
    Generate SQL insert statements for Question table.
    
    Constraints:
    - QuestionID: 1 to 2500
    - 400 Multiple Choice questions
    - 400 True/False questions
    - 400 Text questions
    - ExamID: 1 to 25
    - CourseID: 1 to 22
    """
    # Open the output file to write SQL inserts
    with open(output_file, 'w', encoding='utf-8') as f:
        question_count = {
            'multiple_choice': 0,
            'true_false': 0,
            'text': 0
        }
        
        # Generate questions
        for question_id in range(1, 2501):
            # Determine question type
            if question_count['multiple_choice'] < 400:
                generator = generate_multiple_choice_question
                question_type = 'multiple_choice'
            elif question_count['true_false'] < 400:
                generator = generate_true_false_question
                question_type = 'true_false'
            elif question_count['text'] < 400:
                generator = generate_text_question
                question_type = 'text'
            else:
                break  # Stop if we've generated all required question types
            
            # Generate question details
            question_text, correct_answer, best_answer, multiple_choice, true_false, text = generator(question_id)
            
            # Randomly assign ExamID and CourseID
            exam_id = random.randint(1, 25)
            course_id = random.randint(1, 22)
            
            # Prepare INSERT statement
            insert_stmt = (
                f"INSERT INTO Question (QuestionID, QuestionText, CorrectAnswer, BestAnswer, "
                f"MultipleChoice, TrueFalse, Text, ExamID, CourseID) VALUES "
                f"({question_id}, '{question_text.replace("'", "''")}', "
                f"'{correct_answer.replace("'", "''")}', '{best_answer.replace("'", "''")}', "
                f"'{multiple_choice}', '{true_false}', '{text}', {exam_id}, {course_id});\n"
            )
            
            # Write to file
            f.write(insert_stmt)
            
            # Update question type count
            question_count[question_type] += 1
        
        print(f"SQL insert statements generated in {output_file}")
        print("\nGeneration Statistics:")
        print(question_count)

# Run the generation
generate_question_inserts()
