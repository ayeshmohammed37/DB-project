
CREATE PROCEDURE GetRandomQuestionPool
AS
BEGIN
    DECLARE @RandomQuestions TABLE (
        QuestionID INT,
        QuestionText NVARCHAR(MAX),
        CorrectAnswer NVARCHAR(MAX),
        BestAnswer NVARCHAR(MAX),
        QuestionType NVARCHAR(50)
    )

    DECLARE @QuestionCount INT
    SET @QuestionCount = FLOOR(RAND() * 101) + 100

    INSERT INTO @RandomQuestions (
        QuestionID, 
        QuestionText, 
        CorrectAnswer, 
        BestAnswer, 
        QuestionType
    )
    SELECT TOP (@QuestionCount)
        QuestionID,
        QuestionText,
        CorrectAnswer,
        BestAnswer,
        CASE 
            WHEN MultipleChoice IS NOT NULL AND MultipleChoice <> '' THEN 'MultipleChoice'
            WHEN TrueFalse IS NOT NULL AND TrueFalse <> '' THEN 'TrueFalse'
            WHEN [Text] IS NOT NULL AND [Text] <> '' THEN 'Text'
            ELSE 'Undefined'
        END AS QuestionType
    FROM Question
    WHERE 
        MultipleChoice IS NOT NULL AND MultipleChoice <> ''
        OR TrueFalse IS NOT NULL AND TrueFalse <> ''
        OR [Text] IS NOT NULL AND [Text] <> ''
    ORDER BY NEWID()

    SELECT 
        QuestionID,
        QuestionText,
        CorrectAnswer,
        BestAnswer,
        QuestionType
    FROM @RandomQuestions
END


EXEC GetRandomQuestionPool



CREATE PROCEDURE CreateExamForInstructor
    @InstructorID INT,
    @ExamID INT,
    @MultipleChoiceCount INT,
    @TrueFalseCount INT,
    @TextCount INT
AS
BEGIN
    -- Validate the instructor's courses
    IF NOT EXISTS (
        SELECT 1 FROM InstructorCourse ic
        JOIN Question q ON q.CourseID = ic.CourseID
        WHERE ic.InstructorID = @InstructorID
    )
    BEGIN
        RAISERROR('Instructor has no associated courses with questions.', 16, 1);
        RETURN;
    END

    -- Display Multiple Choice Questions
    SELECT TOP (@MultipleChoiceCount) 
        q.QuestionID,
        q.QuestionText,
        q.MultipleChoice,
        q.CourseID
    FROM Question q
    JOIN InstructorCourse ic ON q.CourseID = ic.CourseID
    WHERE ic.InstructorID = @InstructorID 
      AND q.MultipleChoice IS NOT NULL AND q.MultipleChoice <> ''
    ORDER BY NEWID();

    -- Display True/False Questions
    SELECT TOP (@TrueFalseCount) 
        q.QuestionID,
        q.QuestionText,
        q.TrueFalse,
        q.CourseID
    FROM Question q
    JOIN InstructorCourse ic ON q.CourseID = ic.CourseID
    WHERE ic.InstructorID = @InstructorID 
      AND q.TrueFalse IS NOT NULL AND q.TrueFalse <> ''
    ORDER BY NEWID();

    -- Display Text Questions
    SELECT TOP (@TextCount) 
        q.QuestionID,
        q.QuestionText,
        q.[Text],
        q.CourseID
    FROM Question q
    JOIN InstructorCourse ic ON q.CourseID = ic.CourseID
    WHERE ic.InstructorID = @InstructorID 
      AND q.[Text] IS NOT NULL AND q.[Text] <> ''
    ORDER BY NEWID();
END


EXEC CreateExamForInstructor 
    @InstructorID = 3, 
    @ExamID = 100, 
    @MultipleChoiceCount = 30, 
    @TrueFalseCount = 10, 
    @TextCount = 5


SELECT * FROM Course
SELECT * FROM Question


CREATE VIEW CourseExamQuestions AS
SELECT 
    c.CourseID,
    c.Name AS CourseName,
    e.ExamID,
    e.StartTime,
    e.EndTime,
    e.Year,
    e.ex_Type,
    q.QuestionID,
    q.QuestionText,
    CASE 
        WHEN q.MultipleChoice IS NOT NULL AND q.MultipleChoice <> '' THEN 'MultipleChoice'
        WHEN q.TrueFalse IS NOT NULL AND q.TrueFalse <> '' THEN 'TrueFalse'
        WHEN q.[Text] IS NOT NULL AND q.[Text] <> '' THEN 'Text'
        ELSE 'Undefined'
    END AS QuestionType,
    q.CorrectAnswer,
    q.BestAnswer
FROM 
    Course c
JOIN 
    Exam e ON c.ExamID = e.ExamID
JOIN 
    Question q ON q.CourseID = c.CourseID



SELECT * FROM CourseExamQuestions


CREATE VIEW IntakeStudentTrackView AS
SELECT 
    i.IntakeID,
    i.IntakeName,
    s.StudentID,
    s.Name AS StudentName,
    s.Email,
    s.Phone,
    t.TrackID,
    t.Name AS TrackName,
    m.Name AS TrackManagerName
FROM 
    Intake i
LEFT JOIN 
    Student s ON s.IntakeID = i.IntakeID
LEFT JOIN 
    Track t ON s.TrackID = t.TrackID
LEFT JOIN 
    Manager m ON t.ManagerID = m.ManagerID


SELECT * FROM IntakeStudentTrackView



CREATE PROCEDURE GenerateStudentReportByID
    @StudentID INT
AS
BEGIN
    SELECT 
        s.Name AS StudentName, 
        s.Email AS StudentEmail, 
        c.Name AS CourseName, 
        c.CourseID AS CourseID,
        --e.ExamName AS ExamName,
		e.TotalTime AS TotalTime,
        e.StartTime AS ExamStartTime,
        e.EndTime AS ExamEndTime,
        e.ExamId AS ExamID,
        i.Name AS InstructorName,
        i.Email AS InstructorEmail,
        i.Phone AS InstructorPhone
    FROM Student s
    JOIN StudentCourse sc ON s.StudentID = sc.StudentID
    JOIN Course c ON sc.CourseID = c.CourseID
    LEFT JOIN Exam e ON  c.CourseID = e.ExamID
    LEFT JOIN InstructorCourse ic ON c.CourseID = ic.CourseID
    LEFT JOIN Instructor i ON ic.InstructorID = i.InstructorID
    WHERE s.StudentID = @StudentID;
END

Execute GenerateStudentReportBYID 30;


CREATE PROCEDURE GetExamDetailsByID
    @ExamID INT 
AS
BEGIN
    SELECT 
        e.ExamID,
        --e.ExamName,
        e.StartTime,
        e.EndTime,
        e.TotalTime,
        --e.Corrective,
		e.ex_Type,
        e.Year,
        c.Name
    FROM 
        Exam e
    INNER JOIN 
        Course c ON e.ExamID = c.ExamID
    WHERE 
        e.ExamID = @ExamID;

    SELECT 
        eq.QuestionID,
        q.QuestionText
    FROM 
        Question eq
    INNER JOIN 
        Question q ON eq.QuestionID = q.QuestionID
    WHERE 
        eq.ExamID = @ExamID;
END

EXEC GetExamDetailsByID @ExamID = 10;


CREATE PROCEDURE SearchExamsByCourse
    @CourseName VARCHAR(255)
AS
BEGIN
    SELECT E.ExamID, C.Name, E.StartTime, E.EndTime, E.TotalTime
    FROM Exam E
    JOIN Course C ON E.ExamID = C.ExamID
    WHERE C.Name = @CourseName
END;

execute SearchExamsByCourse'Course 1: Database Systems';

CREATE PROCEDURE GetStudentCountPerCourse
AS
BEGIN
    SELECT 
        c.Name AS CourseName,
        COUNT(sc.StudentID) AS StudentCount
    FROM 
        Course c
    LEFT JOIN 
        StudentCourse sc ON c.CourseID = sc.CourseID
    GROUP BY 
        c.Name
    ORDER BY 
        StudentCount DESC;
END;

Execute GetStudentCountPerCourse


CREATE PROCEDURE GetExamAverage
    @ExamID INT
AS
BEGIN
    SELECT
        AVG(CASE 
            WHEN C.MaxDegree IS NOT NULL AND C.MinDegree IS NOT NULL THEN 
                (C.MaxDegree + C.MinDegree) / 2 
            ELSE 0 
        END) AS AverageScore
    FROM Exam E
    INNER JOIN Course C ON E.ExamID = C.CourseId
    WHERE E.ExamID = @ExamID;
END;

Execute GetExamAverage 4



CREATE PROCEDURE AddStudent
    @StudentID INT,
    @Name VARCHAR(100),
    @Email VARCHAR(100),
    @Phone VARCHAR(15)
AS
BEGIN
    INSERT INTO Student (StudentID, Name, Email, Phone)
    VALUES (@StudentID, @Name, @Email, @Phone);
END;

AddStudent 2000,'fady','fadyemad@gmail.com','01013341812'

select * from student

CREATE PROCEDURE DeleteStudent
    @StudentID INT
AS
BEGIN
    DELETE FROM StudentCourse WHERE StudentID = @StudentID;
    DELETE FROM Student WHERE StudentID = @StudentID;
    PRINT 'Student and related records deleted successfully.';
END;

==>DeleteStudent 2000


=========================
 	TRIGGERS
	
	CREATE TRIGGER trg_NotifyNewStudent
ON Student
AFTER INSERT
AS
BEGIN
    PRINT 'A new student has been added.';
END;

==> AddStudent 2000,'fady','fadyemad@gmail.com','01013341812'



CREATE TRIGGER trg_AfterStudentDelete
ON Student
AFTER DELETE
AS
BEGIN
    DECLARE @StudentID INT;
    DECLARE @DeletedDate DATETIME;

    SELECT @StudentID = StudentID FROM DELETED;
    SET @DeletedDate = GETDATE();

    PRINT 'Student with ID ' + CAST(@StudentID AS VARCHAR) + ' was deleted at ' + CAST(@DeletedDate AS VARCHAR);
END;


==>DeleteStudent 2000


==================================

CREATE PROCEDURE GetInstructorWithCourse
    @InstructorID INT
AS
BEGIN
    SELECT 
        i.InstructorID,
        i.Name AS InstructorName,
        i.Email AS InstructorEmail,
        i.Phone AS InstructorPhone,
        c.CourseID,
        c.Name AS CourseName,
        c.Description AS CourseDescription
    FROM 
        Instructor i
    JOIN 
        InstructorCourse ic ON i.InstructorID = ic.InstructorID
    JOIN 
        Course c ON ic.CourseID = c.CourseID
    WHERE 
        i.InstructorID = @InstructorID;
END;

==> GetInstructorWithCourse 3

===========================

CREATE PROCEDURE GetStudentsByTrack
    @TrackID INT
AS
BEGIN
    SELECT 
        s.StudentID,
        s.Name AS StudentName,
        s.Email AS StudentEmail,
        s.Phone AS StudentPhone,
        t.Name AS TrackName
    FROM 
        Student s
    JOIN 
        Track t ON s.TrackID = t.TrackID
    WHERE 
        s.TrackID = @TrackID;
END;

==> GetStudentsByTrack 1


==========================

CREATE PROCEDURE UpdateInstructorPhone
    @InstructorID INT,
    @NewPhone VARCHAR(15)
AS
BEGIN
    UPDATE Instructor
    SET Phone = @NewPhone
    WHERE InstructorID = @InstructorID;

    IF @@ROWCOUNT > 0
    BEGIN
        PRINT 'Instructor phone updated successfully.';
    END
    ELSE
    BEGIN
        PRINT 'Error: Instructor not found or phone not updated.';
    END
END;

==> UpdateInstructorPhone 1 , '01248551317'

==================
 views

 CREATE VIEW StudentCourseDetails AS
SELECT 
    s.StudentID,
    s.Name AS StudentName,
    s.Email,
    c.Name AS CourseName
FROM 
    Student s
JOIN 
    StudentCourse sc ON s.StudentID = sc.StudentID
JOIN 
    Course c ON sc.CourseID = c.CourseID;

==> SELECT * FROM StudentCourseDetails;

==========================

CREATE VIEW ExamQuestionDetails AS
SELECT 
    c.name AS ExamName,
    q.QuestionID,
    q.QuestionText,
    q.CorrectAnswer,
    q.ExamID
FROM 
    Question q 
JOIN 
    Course c ON q.ExamID = c.ExamID;

==> SELECT * FROM ExamQuestionDetails;

=============================

CREATE VIEW StudentBranchDetails AS
SELECT 
    s.StudentID,
    s.Name AS StudentName,
    s.Email,
    b.Name AS BranchName,
    m.Name AS ManagerName
FROM 
    Student s
JOIN 
    Branch b ON s.BranchID = b.BranchID
JOIN 
    Manager m ON b.ManagerID = m.ManagerID;

==> SELECT * FROM StudentBranchDetails;

CREATE VIEW ManagerDepartmentDetails AS
SELECT 
    m.ManagerID,
    m.Name AS ManagerName,
    d.DepartmentName
FROM 
    Manager m
JOIN 
    Department d ON m.ManagerID = d.ManagerID;

	==> SELECT * FROM ManagerDepartmentDetails;